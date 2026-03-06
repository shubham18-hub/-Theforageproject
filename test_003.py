# Check if the region picker is present.
def test_region(dash_duo):
    dash_duo.start_server(app)

    # wait for radio buttons
    radio = dash_duo.wait_for_element("#region-filter")

    # confirm region picker exists
    assert radio is not None
