env:
	python3 -m venv env
	source env/bin/activate && \
	pip install --upgrade pip && \
	pip install numpy matplotlib && \
    pip install jupyter ipywidgets && \
    pip install tqdm pandas

notebook:
	source env/bin/activate && jupyter notebook

.PHONY: notebook
