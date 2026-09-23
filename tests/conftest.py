import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fast_zero.app import app
from fast_zero.models import table_registry


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')

    # Criando metadata da tabela
    table_registry.metadata.create_all(engine)

    # abrindo session para troca de comunic.
    with Session(engine) as session:
        yield session

    # removendo para limpar db
    table_registry.metadata.drop_all(engine)
