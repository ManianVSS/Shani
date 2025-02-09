import * as React from "react";
import { PieChart } from "@mui/x-charts/PieChart";
import { useDrawingArea } from "@mui/x-charts/hooks";
import { styled } from "@mui/material/styles";

export default function PieChartComponent(props) {
  const data = props.data;
  const size = {
    width: 600,
    height: 300,
  };

  const StyledText = styled("text")(({ theme }) => ({
    fill: theme.palette.text.primary,
    textAnchor: "middle",
    dominantBaseline: "central",
    fontSize: 20,
  }));

  function PieCenterLabel({ children }) {
    const { width, height, left, top } = useDrawingArea();
    return (
      <StyledText x={left + width / 2} y={top + height / 2}>
        {children}
      </StyledText>
    );
  }
  return (
    <PieChart
      series={[{ data, innerRadius: 80 }]}
      {...size}
      colors={["#ffeb99", "#99ff99", "#ffb3b3"]}
    >
      <PieCenterLabel>{props.label}</PieCenterLabel>
    </PieChart>
  );
}
