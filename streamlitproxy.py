def setup_streamlit_proxy():
  return {
    'command': ['streamlit', 'hello', '--server.headless', 'True', '--server.enableCORS', 'False', '--server.port', '{port}']
  }
