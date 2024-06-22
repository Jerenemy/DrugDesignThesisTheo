try:
    import dgl
    import dgllife
    print("dgl version:", dgl.__version__)
    print("dgllife version:", dgllife.__version__)
    print("Import successful!")
except ModuleNotFoundError as e:
    print("ModuleNotFoundError:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
