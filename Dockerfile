FROM continuumio/miniconda3
RUN conda create -n env python=3.6
RUN echo "source activate env" > ~/.bashrc

ENV PATH /opt/conda/envs/env/bin:$PATH

WORKDIR /home/recipe_allocation/

COPY . .

CMD ["python", "main.py","-p", "./data/","-o","orders.json","-s","stock.json"]