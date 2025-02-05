import React, { useState } from "react";
import { Button, Col, Form, Row, Table } from "react-bootstrap";
import Heading from "../../components/Heading";
import SubHeading from "../../components/SubHeading";

const GrowthTarget = () => {
  const [NumOfDevices, setNumOfDevices] = useState(500);
  const [patientReviewDuration, setPatientReviewDuration] = useState(30);
  const [show, setShow] = useState(false);
  const [allData, setAllData] = useState({
    numberOfClients: 0,
    numberOfActiveMonitors: 0,
    numberFOfPatientReviewsInAnHour_Device: 0,
    numberFOfPatientReviewsInAn24_Device: 0,
    numberFOfPatientReviewsInAn24_Device_allDevices: 0,
    numberFOfPatientReviewsIn90Days: 0,
    numberOfCentralWorkstation: 0,
    numberOfPatientReviews_day_workstation: 0,
    numberOfTotalPatientReviewsIn24Hour_workstation: 0,
    numberFOfPatientReviewsIn90Days_2: 0,
    totalNumberOfPatientReviews_hour: 0,
    totalNumberOfPatientReviewsFor90Day: 0,
  });
  const handleSubmit = (event) => {
    event.preventDefault();
    setAllData({
      numberOfClients: NumOfDevices * 2,
      numberOfActiveMonitors: NumOfDevices * 0.75,
      numberFOfPatientReviewsInAnHour_Device: 60 / patientReviewDuration,
      numberFOfPatientReviewsInAn24_Device: (60 / patientReviewDuration) * 24,
      numberFOfPatientReviewsInAn24_Device_allDevices:
        (60 / patientReviewDuration) * 24 * (NumOfDevices * 0.75),
      numberFOfPatientReviewsIn90Days:
        (60 / patientReviewDuration) * 24 * (NumOfDevices * 0.75) * 90,
      numberOfCentralWorkstation: NumOfDevices,
      numberOfPatientReviews_day_workstation: (60 / patientReviewDuration) * 24,
      numberOfTotalPatientReviewsIn24Hour_workstation:
        (60 / patientReviewDuration) * 24 * NumOfDevices,
      numberFOfPatientReviewsIn90Days_2:
        (60 / patientReviewDuration) * 24 * NumOfDevices * 90,
      totalNumberOfPatientReviews_hour:
        ((60 / patientReviewDuration) * 24 * (NumOfDevices * 0.75) +
          (60 / patientReviewDuration) * 24 * NumOfDevices) /
        24,
      totalNumberOfPatientReviewsFor90Day:
        (60 / patientReviewDuration) * 24 * (NumOfDevices * 0.75) * 90 +
        (60 / patientReviewDuration) * 24 * NumOfDevices * 90,
    });
    setShow(true);
  };

  return (
    <div>
      <Heading heading="NGP Growth Target Calculator" />
      <Form style={{ marginBottom: "15px" }} onSubmit={handleSubmit}>
        <Row className="mb-3">
          <Form.Group as={Col} md="4">
            <Form.Label>Number of Devices</Form.Label>
            <Form.Control
              required
              type="number"
              placeholder="# of devices"
              defaultValue="500"
              onChange={(event) => setNumOfDevices(event.target.value)}
            />
            <Form.Control.Feedback>Looks good!</Form.Control.Feedback>
          </Form.Group>
          <Form.Group as={Col} md="4">
            <Form.Label>Duration of a Patient Review(min)</Form.Label>
            <Form.Control
              required
              type="number"
              placeholder="# of devices"
              defaultValue="30"
              onChange={(event) => setPatientReviewDuration(event.target.value)}
            />
            <Form.Control.Feedback>Looks good!</Form.Control.Feedback>
          </Form.Group>
        </Row>
        <Button style={{ backgroundColor: "#404040" }} type="submit">
          Calculate
        </Button>
      </Form>
      {show ? (
        <>
          <Table striped bordered hover>
            <tbody>
              <tr>
                <th>Number of Clients</th>
                <td>{allData.numberOfClients}</td>
              </tr>
              <tr>
                <th>Number of active monitors</th>
                <td>{allData.numberOfActiveMonitors}</td>
              </tr>
            </tbody>
          </Table>
          <SubHeading heading="Breakup for Bedside screen(Workflow1)" />
          <Table striped bordered hover>
            <tbody>
              <tr>
                <th>Number of patient reviews in an Hour/Device</th>
                <td>{allData.numberFOfPatientReviewsInAnHour_Device}</td>
              </tr>
              <tr>
                <th>Number of patient reviews in 24 Hour/Device</th>
                <td>{allData.numberFOfPatientReviewsInAn24_Device}</td>
              </tr>
              <tr>
                <th>Number of patient reviews in 24 Hour(All the devices)</th>
                <td>
                  {allData.numberFOfPatientReviewsInAn24_Device_allDevices}
                </td>
              </tr>
              <tr>
                <th>Number of patient reviews in 90 days</th>
                <td>{allData.numberFOfPatientReviewsIn90Days}</td>
              </tr>
            </tbody>
          </Table>
          <SubHeading heading="Breakup for Workstation screen(Workflow2)" />
          <Table striped bordered hover>
            <tbody>
              <tr>
                <th>Number of Central Workstation</th>
                <td>{allData.numberOfCentralWorkstation}</td>
              </tr>
              <tr>
                <th>Number of patient reviews/day/workstation</th>
                <td>{allData.numberOfPatientReviews_day_workstation}</td>
              </tr>
              <tr>
                <th>Number of total patient reviews in 24 Hour/workstation</th>
                <td>
                  {allData.numberOfTotalPatientReviewsIn24Hour_workstation}
                </td>
              </tr>
              <tr>
                <th>Number of patient reviews in 90 days</th>
                <td>{allData.numberFOfPatientReviewsIn90Days_2}</td>
              </tr>
            </tbody>
          </Table>
          <SubHeading heading="Cumulative details" />
          <Table striped bordered hover>
            <tbody>
              <tr>
                <th>Total Number of Patient Reviews/hour</th>
                <td>{allData.totalNumberOfPatientReviews_hour}</td>
              </tr>
              <tr>
                <th>Total Number of Patient Reviews for 90 day</th>
                <td>
                  <b>{allData.totalNumberOfPatientReviewsFor90Day}</b>
                </td>
              </tr>
            </tbody>
          </Table>
        </>
      ) : (
        <></>
      )}
    </div>
  );
};

export default GrowthTarget;
