import React from "react";
import { Line } from "react-chartjs-2";

const TokenChart = ({ data }) => {
  const chartData = {
    labels: data.map((item) => item.time),
    datasets: [
      {
        label: "Price",
        data: data.map((item) => item.price),
        borderColor: "rgba(75,192,192,1)",
        borderWidth: 2,
      },
    ],
  };

  return <Line data={chartData} />;
};

export default TokenChart;
