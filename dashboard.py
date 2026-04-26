import pandas as pd
import plotly.express as px


def show_dashboard(data):

    if not data:
        return None

    try:
        # Works when query returns 2 columns
        # Example: Product, Sales
        if len(data[0]) == 2:

            df = pd.DataFrame(data, columns=["Category", "Value"])

            fig = px.bar(
                df,
                x="Category",
                y="Value",
                title="Analytics Dashboard",
                text="Value"
            )

            fig.update_layout(
                xaxis_title="Category",
                yaxis_title="Value",
                template="plotly_dark"
            )

            return df, fig

        else:
            return None

    except Exception as e:
        print("Dashboard Error:", e)
        return None