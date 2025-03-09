import pandas as pd
from docx import Document


def read_csv(temp_file, uploaded_file, file_name):
    """
    From csv file read data. Convert to pandas df and creates new column.
    Returns new column.

    Args:
        temp_file: file created in tep folder
        uploaded_file: file name whitch are uploaded
        file_name: uploaded file name
    """
    with open(temp_file, "wb") as f:
        f.write(uploaded_file.getvalue())

    df = pd.read_csv(f"data/temp_files/{file_name}")
    df["id_overview"] = df["id"].astype("str") + " " + df["overview"]

    df_id_overview = df[["id_overview"]]

    return df_id_overview


def read_excel(temp_file, uploaded_file, file_name):
    """
    From excel file read data. Convert to pandas df and creates new column.
    Returns new column.

    Args:
        temp_file: file created in tep folder
        uploaded_file: file name whitch are uploaded
        file_name: uploaded file name
    """
    with open(temp_file, "wb") as f:
        f.write(uploaded_file.getvalue())

    df = pd.read_excel(f"data/temp_files/{file_name}")
    df["id_overview"] = df["id"].astype("str") + " " + df["overview"]
    df_id_overview = df[["id_overview"]]

    return df_id_overview


def read_word(temp_file, uploaded_file, file_name):
    """
    From docx file read data. Convert to pandas df and creates new column.
    Returns new column.

    Args:
        temp_file: file created in tep folder
        uploaded_file: file name whitch are uploaded
        file_name: uploaded file name
    """
    with open(temp_file, "wb") as f:
        f.write(uploaded_file.getvalue())

    document = Document(f"data/temp_files/{file_name}")
    table = document.tables[0]
    df = pd.DataFrame([[cell.text for cell in row.cells] for row in table.rows])
    df = df.rename(columns=df.iloc[0]).drop(df.index[0]).reset_index(drop=True)
    df["id_overview"] = df["id"].astype("str") + " " + df["overview"]
    df_id_overview = df[["id_overview"]]

    return df_id_overview
