import React from "react";
import { Typography } from "../components/Wrappers";
import Widget from "../components/Widget";
import { Grid } from "@material-ui/core";
import { useTheme } from "@material-ui/styles";
import useStyles from "./styles";
import { LineChart, Line } from "recharts";

const FeatureCard = (props) => {
  var classes = useStyles();
  var theme = useTheme();
  return (
    <Widget
      title={props.data.name}
      upperTitle
      bodyClass={classes.fullHeightBody}
      className={classes.card}
      disableWidgetMenu
    >
      <div className={classes.visitsNumberContainer}>
        {/* <Typography size="xl" weight="medium">
          678
        </Typography> */}
        {/* <LineChart
          width={55}
          height={30}
          data={[
            { value: 10 },
            { value: 15 },
            { value: 10 },
            { value: 17 },
            { value: 18 },
          ]}
          margin={{ left: theme.spacing(2) }}
        >
          <Line
            type="natural"
            dataKey="value"
            stroke={theme.palette.success.main}
            strokeWidth={2}
            dot={false}
          />
        </LineChart> */}
      </div>
      <Grid
        container
        direction="row"
        justify="space-between"
        alignItems="center"
      >
        <Grid item>
          <Typography color="text" colorBrightness="secondary">
            Score
          </Typography>
          <Typography size="md">{props.data.score}</Typography>
        </Grid>
        <Grid item>
          <Typography color="text" colorBrightness="secondary">
            Weight
          </Typography>
          <Typography size="md">{props.data.weight}</Typography>
        </Grid>
      </Grid>
    </Widget>
  );
};

export default FeatureCard;
