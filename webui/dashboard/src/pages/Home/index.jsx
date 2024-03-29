import React from "react";
import { Row, Col, Container } from "react-bootstrap";
import BatteryGauge from "react-battery-gauge";
import GaugeChart from "react-gauge-chart";
import { axiosClient } from "../../api/AxiosInstance";
import {
  Grid,
  LinearProgress,
  Select,
  OutlinedInput,
  MenuItem,
} from "@material-ui/core";
import { useTheme } from "@material-ui/styles";
import {
  ResponsiveContainer,
  ComposedChart,
  AreaChart,
  LineChart,
  Line,
  Area,
  PieChart,
  Pie,
  Cell,
  YAxis,
  XAxis,
  BarChart,
  Bar,
  CartesianGrid,
  Tooltip,
  Legend,
} from "recharts";

// styles
import useStyles from "./styles";

import mock from "./mock";
import Widget from "../../components/Widget";
import PageTitle from "../../components/PageTitle";
import { Typography } from "../../components/Wrappers";
import Dot from "../../components/Sidebar/components/Dot";
import Table from "./components/Table/Table";
import BigStat from "./components/BigStat/BigStat";
import CustomCarousel from "../../components/CustomCarousel";
import FeatureCard from "../../components/FeatureCard";
const barChartData = [
  {
    name: "Page A",
    uv: 4000,
  },
  {
    name: "Page B",
    uv: 3000,
  },
  {
    name: "Page C",
    uv: 2000,
  },
  {
    name: "Page D",
    uv: 2780,
  },
  {
    name: "Page E",
    uv: 1890,
  },
  {
    name: "Page F",
    uv: 2390,
  },
  {
    name: "Page G",
    uv: 3490,
  },
];
const mainChartData = getMainChartData();
const PieChartData = [
  { name: "Group A", value: 400, color: "primary" },
  { name: "Group B", value: 300, color: "secondary" },
  { name: "Group C", value: 300, color: "warning" },
  { name: "Group D", value: 200, color: "success" },
];
const Home = () => {
  var [mainChartState, setMainChartState] = React.useState("monthly");
  const [testsData, setTestsData] = React.useState({
    total: 0,
    automated: 0,
    manual: 0,
  });
  const [useCaseData, setUseCaseData] = React.useState({
    total: 0,
    draft: 0,
    inreview: 0,
    approved: 0,
  });
  const [score, setScore] = React.useState([]);
  const [completion, setCompletion] = React.useState([]);

  const TestsPieChartData = [
    { name: "Automated", value: testsData.automated, color: "success" },
    { name: "Manual", value: testsData.manual, color: "secondary" },
  ];
  const UseCasePieChartData = [
    { name: "Draft", value: useCaseData.draft, color: "primary" },
    { name: "In Review", value: useCaseData.inreview, color: "secondary" },
    { name: "Approved", value: useCaseData.approved, color: "success" },
  ];
  var classes = useStyles();
  var theme = useTheme();
  React.useEffect(() => {
    let testsData = { total: 0, automated: 0, manual: 0 };
    axiosClient.get("/testdesign/api/testcases/").then((response) => {
      response.data.results.map((item) => {
        testsData.total += 1;
        if (item.automated) {
          testsData.automated += 1;
        } else {
          testsData.manual += 1;
        }
      });
      setTestsData(testsData);
    });
  }, []);
  React.useEffect(() => {
    let useCaseData = { total: 0, draft: 0, inreview: 0, approved: 0 };
    axiosClient.get("/requirements/api/use_cases/").then((response) => {
      response.data.results.map((item) => {
        useCaseData.total += 1;
        if (item.status === "DRAFT") {
          useCaseData.draft += 1;
        } else if (item.status === "APPROVED") {
          useCaseData.approved += 1;
        } else {
          useCaseData.inreview += 1;
        }
      });
      setUseCaseData(useCaseData);
    });
  }, []);
  React.useEffect(() => {
    axiosClient.get("/execution/api/score/").then((response) => {
      setScore(response.data);
    });
  }, []);
  React.useEffect(() => {
    let data = {};
    axiosClient.get("/execution/api/completion/").then((response) => {
      data = response.data;
      data.use_case_category_completion.map((item) => {
        item.completion = item.completion * 100;
      });
      setCompletion(data);
    });
  }, []);
  return (
    <>
      <Container>
        <Row style={{ marginBottom: "10px" }}>
          <Col sm={4}>
            <div
              style={{
                width: "80%",
                marginTop: "20%",
                marginBottom: "5px",
                marginLeft: "8%",
              }}
            >
              <Row>
                <Col
                  sm={8}
                  style={{
                    background: "gray",
                    color: "white",
                    border: "1px solid gray",
                    borderRadius: "25px",
                    borderTopRightRadius: "0px",
                    borderTopLeftRadius: "25px",
                    borderBottomRightRadius: "0px",
                    borderBottomLeftRadius: "25px",
                  }}
                >
                  <h4 style={{ marginTop: "2%" }}>Total Score</h4>
                </Col>
                <Col
                  sm={4}
                  style={{
                    border: "1px solid gray",
                    borderTopRightRadius: "25px",
                    borderTopLeftRadius: "0px",
                    borderBottomRightRadius: "25px",
                    borderBottomLeftRadius: "0px",
                  }}
                >
                  <h4 style={{ marginTop: "5%" }}>
                    {score.score === undefined ? 0 : score.score.toFixed(0)}%
                  </h4>
                </Col>
              </Row>
            </div>
            <div>
              <GaugeChart
                id="gauge-chart3"
                nrOfLevels={3}
                colors={["red", "green"]}
                arcWidth={0.3}
                percent={
                  score.score === undefined ? 0 : score.score.toFixed(0) / 100
                }
                textColor={"black"}
              />
            </div>
          </Col>
          <Col sm={8}>
            <Widget
              title="Usecase Category Scores"
              upperTitle
              bodyClass={classes.fullHeightBody}
              className={classes.card}
              disableWidgetMenu
            >
              <BarChart
                width={650}
                height={300}
                // data={barChartData}
                data={score?.use_case_category_scores}
                layout="vertical"
                margin={{
                  top: 5,
                  right: 30,
                  left: 20,
                  bottom: 5,
                }}
              >
                <CartesianGrid strokeDasharray="3 3" horizontal={false} />
                <XAxis
                  type="number"
                  axisLine={false}
                  stroke="#a0a0a0"
                  domain={[0, 100]}
                  ticks={[0, 25, 50, 75, 100]}
                  strokeWidth={0.5}
                />
                <YAxis dataKey="name" type="category" width={90} />
                <Tooltip />
                <Legend />
                {/* <Bar dataKey="pv" fill="#8884d8" /> */}
                <Bar
                  dataKey="score"
                  fill="#82ca9d"
                  label={{ position: "centerTop", fill: "#404040" }}
                  unit="%"
                />
              </BarChart>
            </Widget>
          </Col>
        </Row>
      </Container>
      <Container>
        <Row style={{ marginBottom: "10px" }}>
          <Col className="col-md-6">
            <Widget
              title={"Total Tests - " + testsData.total}
              upperTitle
              className={classes.card}
              disableWidgetMenu
            >
              <Grid container spacing={2}>
                <Grid item xs={6}>
                  <ResponsiveContainer width="100%" height={144}>
                    <PieChart margin={{ left: theme.spacing(2) }}>
                      <Pie
                        data={TestsPieChartData}
                        innerRadius={45}
                        outerRadius={60}
                        dataKey="value"
                      >
                        {TestsPieChartData.map((entry, index) => (
                          <Cell
                            key={`cell-${index}`}
                            fill={theme.palette[entry.color].main}
                          />
                        ))}
                      </Pie>
                    </PieChart>
                  </ResponsiveContainer>
                </Grid>
                <Grid item xs={6}>
                  <div className={classes.pieChartLegendWrapper}>
                    {TestsPieChartData.map(({ name, value, color }, index) => (
                      <div key={color} className={classes.legendItemContainer}>
                        <Dot color={color} />
                        <Typography style={{ whiteSpace: "nowrap" }}>
                          &nbsp;{name}&nbsp;
                        </Typography>
                        <Typography color="text" colorBrightness="secondary">
                          &nbsp;{value}
                        </Typography>
                      </div>
                    ))}
                  </div>
                </Grid>
              </Grid>
            </Widget>
          </Col>
          <Col className="col-md-6">
            <Widget
              title={"Total Use Cases - " + useCaseData.total}
              upperTitle
              className={classes.card}
              disableWidgetMenu
            >
              <Grid container spacing={2}>
                <Grid item xs={6}>
                  <ResponsiveContainer width="100%" height={144}>
                    <PieChart margin={{ left: theme.spacing(2) }}>
                      <Pie
                        data={UseCasePieChartData}
                        innerRadius={45}
                        outerRadius={60}
                        dataKey="value"
                      >
                        {UseCasePieChartData.map((entry, index) => (
                          <Cell
                            key={`cell-${index}`}
                            fill={theme.palette[entry.color].main}
                          />
                        ))}
                      </Pie>
                    </PieChart>
                  </ResponsiveContainer>
                </Grid>
                <Grid item xs={6}>
                  <div className={classes.pieChartLegendWrapper}>
                    {UseCasePieChartData.map(
                      ({ name, value, color }, index) => (
                        <div
                          key={color}
                          className={classes.legendItemContainer}
                        >
                          <Dot color={color} />
                          <Typography style={{ whiteSpace: "nowrap" }}>
                            &nbsp;{name}&nbsp;
                          </Typography>
                          <Typography color="text" colorBrightness="secondary">
                            &nbsp;{value}
                          </Typography>
                        </div>
                      )
                    )}
                  </div>
                </Grid>
              </Grid>
            </Widget>
          </Col>
        </Row>
      </Container>
      {/* <Container>
        <Row style={{ marginBottom: "10px" }}>
          <Col sm={4}>
            <Widget upperTitle className={classes.card} disableWidgetMenu>
              <Typography color="text" colorBrightness="secondary">
                Total Score
              </Typography>
              <Typography size="md">{score.score}</Typography>
            </Widget>
          </Col>
          <Col sm={8}>
            <CustomCarousel
              component={FeatureCard}
              data={score?.use_case_category_scores}
            />
          </Col>
        </Row>
      </Container> */}

      {/* <Container>
        <Row style={{ marginBottom: "10px" }}>
          <Col>
            <Widget
              title="Use case Status"
              upperTitle
              bodyClass={classes.fullHeightBody}
              className={classes.card}
              disableWidgetMenu
            >
              <div>
                <BatteryGauge
                  customization={{
                    batteryMeter: {
                      fill: "green",
                      lowBatteryValue: 40,
                      lowBatteryFill: "red",
                      outerGap: 1,
                      noOfCells: 1,
                      interCellsGap: 1,
                    },
                  }}
                  animated={true}
                  size={280}
                />
              </div>
            </Widget>
          </Col>
          <Col>
            <Widget
              title="Test Status"
              upperTitle
              bodyClass={classes.fullHeightBody}
              className={classes.card}
              disableWidgetMenu
            >
              <GaugeChart
                id="gauge-chart3"
                nrOfLevels={3}
                colors={["red", "green"]}
                arcWidth={0.3}
                percent={
                  score.score === undefined ? 0 : score.score.toFixed(0) / 100
                }
                textColor={"black"}
              />
            </Widget>
          </Col>
        </Row>
      </Container> */}
      <Container>
        <Row style={{ marginBottom: "10px" }}>
          <Col sm={4}>
            <div
              style={{
                width: "80%",
                marginTop: "20%",
                marginBottom: "5px",
                marginLeft: "8%",
              }}
            >
              <Row>
                <Col
                  sm={8}
                  style={{
                    background: "gray",
                    color: "white",
                    border: "1px solid gray",
                    borderRadius: "25px",
                    borderTopRightRadius: "0px",
                    borderTopLeftRadius: "25px",
                    borderBottomRightRadius: "0px",
                    borderBottomLeftRadius: "25px",
                  }}
                >
                  <h4 style={{ marginTop: "2%", fontSize: "20px" }}>
                    Test Completion
                  </h4>
                </Col>
                <Col
                  sm={4}
                  style={{
                    border: "1px solid gray",
                    borderTopRightRadius: "25px",
                    borderTopLeftRadius: "0px",
                    borderBottomRightRadius: "25px",
                    borderBottomLeftRadius: "0px",
                  }}
                >
                  <h4 style={{ marginTop: "5%" }}>
                    {completion.completion === undefined
                      ? 0
                      : (completion.completion * 100).toFixed(0)}
                    %
                  </h4>
                </Col>
              </Row>
            </div>
            <div>
              <GaugeChart
                id="gauge-chart3"
                nrOfLevels={3}
                colors={["#62af95", "#3dac87", "#0caa09"]}
                arcWidth={0.3}
                percent={
                  completion.completion === undefined
                    ? 0
                    : (completion.completion * 100).toFixed(0) / 100
                }
                textColor={"black"}
              />
            </div>
          </Col>
          <Col sm={8}>
            <Widget
              title="Test Completion Status(Usecase Category wise)"
              upperTitle
              bodyClass={classes.fullHeightBody}
              className={classes.card}
              disableWidgetMenu
            >
              <BarChart
                width={650}
                height={300}
                // data={barChartData}
                data={completion?.use_case_category_completion}
                layout="vertical"
                margin={{
                  top: 5,
                  right: 30,
                  left: 20,
                  bottom: 5,
                }}
              >
                <CartesianGrid strokeDasharray="3 3" horizontal={false} />
                <XAxis
                  type="number"
                  axisLine={false}
                  stroke="#a0a0a0"
                  domain={[0, 100]}
                  ticks={[0, 25, 50, 75, 100]}
                  strokeWidth={0.5}
                />
                <YAxis dataKey="name" type="category" width={90} />
                <Tooltip />
                <Legend />
                {/* <Bar dataKey="pv" fill="#8884d8" /> */}
                <Bar
                  dataKey="completion"
                  fill="#40b7a9"
                  label={{ position: "centerTop", fill: "#404040" }}
                  legendType="triangle"
                  unit="%"
                />
              </BarChart>
            </Widget>
          </Col>
        </Row>
      </Container>
    </>
  );
};

export default Home;

// #######################################################################
function getRandomData(length, min, max, multiplier = 10, maxDiff = 10) {
  var array = new Array(length).fill();
  let lastValue;

  return array.map((item, index) => {
    let randomValue = Math.floor(Math.random() * multiplier + 1);

    while (
      randomValue <= min ||
      randomValue >= max ||
      (lastValue && randomValue - lastValue > maxDiff)
    ) {
      randomValue = Math.floor(Math.random() * multiplier + 1);
    }

    lastValue = randomValue;

    return { value: randomValue };
  });
}

function getMainChartData() {
  var resultArray = [];
  var tablet = getRandomData(31, 3500, 6500, 7500, 1000);
  var desktop = getRandomData(31, 1500, 7500, 7500, 1500);
  var mobile = getRandomData(31, 1500, 7500, 7500, 1500);

  for (let i = 0; i < tablet.length; i++) {
    resultArray.push({
      tablet: tablet[i].value,
      desktop: desktop[i].value,
      mobile: mobile[i].value,
    });
  }

  return resultArray;
}
