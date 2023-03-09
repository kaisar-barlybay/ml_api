from api.base import Base
from matplotlib import pyplot as plt
import numpy as np
import os
from pandas import DataFrame
import bokeh.plotting as bp
from bokeh.plotting import show
from bokeh.models import ColumnDataSource
from bokeh.models import HoverTool
import colorsys


def HSVToRGB(h, s, v):
  (r, g, b) = colorsys.hsv_to_rgb(h, s, v)
  return (int(255*r), int(255*g), int(255*b))


def rgb_to_hex(rgb):
  return '#%02x%02x%02x' % rgb


class Visualizer(Base):
  def __init__(self) -> None:
    super().__init__()
    self.output_path = os.path.join(self.drive_letter, 'atlant', 'images')

  def getDistinctColors(self, n):
    huePartition = 1.0 / (n + 1)
    colors = [rgb_to_hex(HSVToRGB(huePartition * value, 1.0, 1.0)) for value in range(0, n)]
    return np.array(colors)

  def plot_horizontal_bar(self, labels: list[str], values: list[float], title: str, x_label: str, y_label: str, **kwargs):
    fig, ax = plt.subplots()
    fig.set_size_inches(kwargs.get('width', 13), kwargs.get('height', 15.5))

    # !fix
    # bar_labels = ['red', 'blue', '_red', 'orange']
    # bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']
    # ax.barh(labels, counts, label=bar_labels, color=bar_colors)

    ax.barh(labels, values)
    ax.set_yticks(np.arange(len(values)))
    plt.xticks(rotation=90)

    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    if kwargs.get('set_y_ticks'):
      ax.set_yticks(np.arange(len(values)), labels=labels)

    bar_text_func = kwargs.get('bar_text_func')
    for i, v in enumerate(values):
      if bar_text_func is not None:
        ax.text(v, i, f'{bar_text_func(i)}', color='black', fontsize=9, ha='left', va='center')
      else:
        ax.text(v, i, f'{values[i]}', color='black', fontsize=9, ha='left', va='center')

    output = kwargs.get('output')
    if output is not None:
      fig.savefig(os.path.join(self.output_path, output), bbox_inches='tight')

  def plot_vertical_bar(self, labels: list[str], values: list[float], title: str, x_label: str, y_label: str, **kwargs):
    fig, ax = plt.subplots()
    fig.set_size_inches(kwargs.get('width', 6), kwargs.get('height', 5))

    # !fix
    bar_labels = ['red', 'blue', '_red', 'orange']
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']
    # ax.barh(labels, counts, label=bar_labels, color=bar_colors)

    ax.bar(labels, values, label=bar_labels, color=bar_colors)
    # ax.set_yticks(np.arange(len(values)))
    plt.xticks(rotation=90)

    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    # bar_text_func = kwargs.get('bar_text_func')
    for i, v in enumerate(values):
      ax.text(i, v, f'{values[i]}', color='black', fontsize=9, ha='center', va='bottom')

    output = kwargs.get('output')
    if output is not None:
      fig.savefig(os.path.join(self.output_path, output), bbox_inches='tight')
    if self.show:
      plt.show()

  def build_bokeh_scatter(self, lda_df: DataFrame, lda_keys: list[int], number_of_clusters: int):
    plot_lda = bp.figure(outer_width=700,
                         outer_height=600,
                         title="LDA topic visualization",
                         tools="pan,wheel_zoom,box_zoom,reset,hover,save",
                         x_axis_type=None, y_axis_type=None, min_border=1)

    plot_kmeans = bp.figure(outer_width=700, outer_height=600,
                            title="KMeans clustering of the description",
                            tools="pan,wheel_zoom,box_zoom,reset,hover,save",
                            x_axis_type=None, y_axis_type=None, min_border=1)
    colors = self.getDistinctColors(number_of_clusters)
    source = ColumnDataSource(data=dict(x=lda_df['x'], y=lda_df['y'],
                                        color=colors[lda_keys],
                                        description=lda_df['description'],
                                        topic=lda_df['topic'],
                                        category=lda_df['category']
                                        )
                              )

    plot_lda.scatter(source=source, x='x', y='y', color='color')
    hover = plot_kmeans.select(dict(type=HoverTool))
    hover = plot_lda.select(dict(type=HoverTool))
    hover.tooltips = {"description": "@description",
                      "topic": "@topic", "category": "@category"}
    show(plot_lda)
