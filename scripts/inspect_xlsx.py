import pandas as pd
import glob

def inspect():
    files = glob.glob('raw/*.xlsx')
    for f in files:
        print(f"File: {f}")
        df = pd.read_excel(f, header=None, nrows=20)
        for idx, row in df.iterrows():
            print(f"Row {idx}: {row.tolist()}")

if __name__ == '__main__':
    inspect()
