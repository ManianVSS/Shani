import React, { useState } from "react";
import { useParams } from "react-router-dom";
import { axiosClientForReliability } from "../../reliabilityApi";
import { Col, Row, Table } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import Heading from "../../components/Heading";
import { PieChart } from "@mui/x-charts";
import PieChartComponent from "../../components/PieChartComponent";

const ReliRun = () => {
  const { relirunID } = useParams();
  const [relirunData, setRelirunData] = useState({});

  React.useEffect(() => {
    axiosClientForReliability
      .get("/execution/api/reliability_runs/" + relirunID + "/")
      .then((response) => {
        setRelirunData(response.data);
      });
  }, []);
  return (
    <>
      <Heading heading={relirunData.name} />
      <Row>
        <Col>
          <Table striped bordered hover>
            <tbody>
              <tr>
                <th>Build name</th>
                <td>{relirunData.build}</td>
              </tr>
              <tr>
                <th>Release name</th>
                <td>{relirunData.release}</td>
              </tr>
              <tr>
                <th>Test name</th>
                <td>{relirunData.testName}</td>
              </tr>
              <tr>
                <th>Test Environment name</th>
                <td>{relirunData.testEnvironmentName}</td>
              </tr>
              <tr>
                <th>Test Environment type</th>
                <td>{relirunData.testEnvironmentType}</td>
              </tr>
            </tbody>
          </Table>
        </Col>
        <Col>
          <Table striped bordered hover>
            <tbody>
              <tr>
                <th>Run name</th>
                <td>{relirunData.name}</td>
              </tr>
              <tr>
                <th>Run started on</th>
                <td>
                  {new Date(relirunData.start_time).toDateString() +
                    " - " +
                    new Date(relirunData.start_time).toLocaleTimeString()}
                </td>
              </tr>
              <tr>
                <th>Run ended on</th>
                <td>
                  {new Date(relirunData.start_time).toDateString() +
                    " - " +
                    new Date(relirunData.start_time).toLocaleTimeString()}
                </td>
              </tr>
              <tr>
                <th>Run status</th>
                {relirunData.status === "COMPLETED" ? (
                  <td style={{ backgroundColor: "#99ff99" }}>
                    {relirunData.status === "IN_PROGRESS"
                      ? "IN PROGRESS"
                      : relirunData.status}
                  </td>
                ) : (
                  <td style={{ backgroundColor: "#ffe6b3" }}>
                    {relirunData.status === "IN_PROGRESS"
                      ? "IN PROGRESS"
                      : relirunData.status}
                  </td>
                )}
              </tr>
            </tbody>
          </Table>
        </Col>
        <Col>
          <Table striped bordered hover>
            <tbody>
              <tr>
                <th>Target iterations</th>
                <td>{relirunData.totalIterationCount}</td>
              </tr>
              <tr>
                <th>Passed iterations</th>
                <td>{relirunData.passedIterationCount}</td>
              </tr>
              <tr>
                <th>Incident count</th>
                <td>{relirunData.incidentCount}</td>
              </tr>
              <tr>
                <th>Target IPTI</th>
                <td>{relirunData.targetIPTE}</td>
              </tr>
              <tr>
                <th>Achieved IPTI</th>
                <td>{relirunData.ipte}</td>
              </tr>
            </tbody>
          </Table>
        </Col>
      </Row>
      <PieChartComponent
        data={[
          { value: 50, label: "Pending Iterations" },
          { value: 40, label: "Passed Iterations" },
          { value: 10, label: "Failed Iterations" },
        ]}
        label={"Execution status"}
      />
    </>
  );
};

export default ReliRun;
