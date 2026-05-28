import json
import plotly.graph_objects as go

def main():
    with open("route_output.json", "r") as f:
        data = json.load(f)

    latitudes = []
    longitudes = []
    labels = []

    for hop in data:
        lat = hop.get("lat")
        lon = hop.get("lon")
        if lat is not None and lon is not None:
            latitudes.append(lat)
            longitudes.append(lon)
            labels.append(f"TTL {hop['ttl']}: {hop['ip']} ({hop['location']})")

    if not latitudes or not longitudes:
        print("Nu s-au gasit coordonate valide in date.")
        return

    fig = go.Figure()

    # punctele
    fig.add_trace(go.Scattergeo(
        lon=longitudes,
        lat=latitudes,
        text=labels,
        mode='markers+text',
        marker=dict(size=8, color='blue'),
        name='Hop-uri'
    ))

    # linia
    fig.add_trace(go.Scattergeo(
        lon=longitudes,
        lat=latitudes,
        mode='lines',
        line=dict(width=2, color='red'),
        name='Traseu'
    ))

    fig.update_layout(
        title="Harta traseului traceroute",
        geo=dict(
            showland=True,
            landcolor="rgb(243, 243, 243)",
            countrycolor="rgb(204, 204, 204)",
            coastlinecolor="rgb(204, 204, 204)",
            projection_type="equirectangular",
        )
    )

    fig.write_html("map.html", auto_open=False)
    print("Harta a fost generata si salvata in 'map.html'.")


if __name__ == "__main__":
    main()
