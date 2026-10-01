import gradio as gr
import pandas as pd


def read_csv(file):
    df = pd.read_csv(file.name)
    return df.head(3)


demo = gr.Interface(
    fn=read_csv,
    inputs=gr.File(file_types=[".csv"]),
    outputs=gr.Dataframe(),
    title="CSV Reader"
)

demo.launch()