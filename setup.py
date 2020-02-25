import setuptools

setuptools.setup(
  name="jupyter-streamlit-server",
  # py_modules rather than packages, since we only have 1 file
  py_modules=['streamlitproxy'],
  entry_points={
      'jupyter_serverproxy_servers': [
          # name = packagename:function_name
          'streamlitserver = streamlitproxy:setup_streamlit_proxy',
      ]
  },
  install_requires=['jupyter-server-proxy'],
)

