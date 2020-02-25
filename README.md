# Docker image running Streamlit proxied through a Jupyter notebook (with JupyterHub support) 

```
docker build -t danlester/jupyterhub-singleuser-streamlit-proxied .
```

Add to jupyterhub_config.py:

```
c.DockerSpawner.image = 'danlester/jupyterhub-singleuser-streamlit-proxied:latest'
c.Spawner.default_url = '/streamlitserver'
```

