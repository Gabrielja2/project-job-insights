from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    results = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    assert results.__contains__(
        {'salary': '2000', 'title': 'Maquinista', 'type': 'trainee'}
    )
