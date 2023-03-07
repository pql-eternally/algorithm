import pynecone as pc

config = pc.Config(
    app_name="qpynecne",
    api_url="http://127.0.0.1:8000",
    db_url="sqlite:///pynecone.db",
    frontend_packages=[
        "react-colorful",
    ],
    env=pc.Env.DEV,
    telemetry_enabled=False,
)
