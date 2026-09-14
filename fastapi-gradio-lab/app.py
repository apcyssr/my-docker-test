import gradio as gr
import seaborn as sns
from fastapi import FastAPI

app = FastAPI()

df = sns.load_dataset("titanic")


@app.get("/")
def read_root():
    return {"message": "FastAPI + Gradio is running!"}


def show_data():
    return df.head(10)


demo = gr.Interface(
    fn=show_data,
    inputs=[],
    outputs=gr.Dataframe(),
    title="Titanic Dataset",
    description="Titanic dataset from Seaborn",
)

app = gr.mount_gradio_app(app, demo, path="/gradio")