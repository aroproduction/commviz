def plot_signal(t, x, title="Signal", discrete=False):
    import plotly.graph_objects as go

    fig = go.Figure()

    if discrete:
        # Stem plot: markers + vertical lines
        for xi, ti in zip(x, t):
            fig.add_trace(
                go.Scatter(
                    x=[ti, ti],
                    y=[0, xi],
                    mode="lines+markers",
                    marker=dict(color="blue", size=8),
                    line=dict(color="blue", width=2),
                    showlegend=False,
                )
            )
    else:
        fig.add_trace(go.Scatter(x=t, y=x, mode="lines", name="Signal"))

    fig.update_layout(
        title=title,
        xaxis_title="Time",
        yaxis_title="Amplitude",
        template="plotly_white",
        height=400,
    )

    return fig
