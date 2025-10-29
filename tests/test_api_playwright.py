import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


def test_api_root(page):
    response = page.goto("http://localhost:8080/")
    assert response.status == 200
    assert "Bienvenue" in page.content()


def test_metrics_endpoint(page):
    response = page.goto("http://localhost:8080/metrics")
    assert response.status == 200
    assert "python_gc_objects_collected_total" in page.content()
