import React, { useEffect, useState } from "react";
import { Button, Col, Form, Row, Table } from "react-bootstrap";
import Heading from "../../components/Heading";
import { chisqInvRt } from "./util";

const ReliTarget = () => {
  const [show, setShow] = useState(false);
  const [MTTR, setMTTR] = useState(0.366666667);
  const [availability, setAvailability] = useState(0.999);
  const [examsPerHour, setExamsPerHour] = useState(1750);
  const [confidence, setConfidence] = useState(0.9);
  const [incidentsAllowed, setIncidentsAllowed] = useState(0);
  const [completedExams, setCompletedExams] = useState(0);
  const [allData, setAllData] = useState({
    mtbf: 0,
    numberOfReviewsForGivenMTBF: 0,
    failureRate: 0,
    chiSquareValue: 0,
    numberOfReviewToCompleteWithoutFailure: 0,
  });

  const handleSubmit = (event) => {
    event.preventDefault();

    getAllValues(
      MTTR,
      availability,
      examsPerHour,
      confidence,
      incidentsAllowed
    );
  };

  const getAllValues = (
    mttr,
    availability,
    examsPerHour,
    confidence,
    incidentsAllowed
  ) => {
    const data_mtbf =
      (Number(availability) * Number(mttr)) / (1 - Number(availability));
    const data_numberofreviewsforgivenmtbf = data_mtbf * Number(examsPerHour);
    const data_failurerate = (1 / data_numberofreviewsforgivenmtbf) * 1000;
    const data_chisquarevalue = chisqInvRt(
      1 - Number(confidence),
      2 * (Number(incidentsAllowed) + 1)
    );

    const data_numberOfReviewToCompleteWithoutFailure =
      (data_chisquarevalue * 1000) / data_failurerate / 2;

    setAllData({
      mtbf: data_mtbf,
      numberOfReviewsForGivenMTBF: data_numberofreviewsforgivenmtbf,
      failureRate: data_failurerate,
      chiSquareValue: data_chisquarevalue,
      numberOfReviewToCompleteWithoutFailure:
        data_numberOfReviewToCompleteWithoutFailure,
    });
    setShow(true);
  };
  //   useEffect(() => {
  //     getAllValues();
  //   }, []);
  return (
    <div>
      <Form style={{ marginBottom: "15px" }} onSubmit={handleSubmit}>
        <Row className="mb-3">
          <Form.Group as={Col} md="4">
            <Form.Label>MTTR(Mean time to recover/repair)</Form.Label>
            <Form.Control
              required
              type="number"
              placeholder="MTTR"
              defaultValue="0.366666667"
              onChange={(event) => setMTTR(event.target.value)}
            />
            <Form.Control.Feedback>Looks good!</Form.Control.Feedback>
          </Form.Group>
          <Form.Group as={Col} md="4">
            <Form.Label>Availability requirement(in %)</Form.Label>
            <Form.Control
              required
              type="number"
              placeholder="Availability"
              defaultValue="99.9"
              onChange={(event) => setAvailability(event.target.value / 100)}
            />
            <Form.Control.Feedback>Looks good!</Form.Control.Feedback>
          </Form.Group>
          <Form.Group as={Col} md="4">
            <Form.Label>Number of Reviews/Iterations/Exams per hour</Form.Label>
            <Form.Control
              required
              type="number"
              placeholder="# of exams/iterations"
              defaultValue="1750"
              onChange={(event) => setExamsPerHour(event.target.value)}
            />
            <Form.Control.Feedback>Looks good!</Form.Control.Feedback>
          </Form.Group>
          <Form.Group as={Col} md="4" controlId="validationCustom02">
            <Form.Label>Confidence interval(in %)</Form.Label>
            <Form.Control
              required
              type="number"
              placeholder="confidence interval"
              defaultValue="90"
              onChange={(event) => setConfidence(event.target.value / 100)}
            />
            <Form.Control.Feedback>Looks good!</Form.Control.Feedback>
          </Form.Group>
          <Form.Group as={Col} md="4">
            <Form.Label>Number of incidents allowed</Form.Label>
            <Form.Control
              required
              type="number"
              placeholder="# of incidents allowed"
              defaultValue="0"
              onChange={(event) => setIncidentsAllowed(event.target.value)}
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
          <Heading heading="Reliability target details" />
          <Table striped bordered hover>
            <tbody>
              <tr>
                <th>MTBF(Mean time between failures)</th>
                <td>{allData.mtbf}</td>
              </tr>
              <tr>
                <th>Number of reviews for given MTBF</th>
                <td>{allData.numberOfReviewsForGivenMTBF}</td>
              </tr>
              <tr>
                <th>Failure rate(Incidents per 1000 reviews)</th>
                <td>
                  <b>{allData.failureRate}</b>
                </td>
              </tr>
              <tr>
                <th>Chi Square value</th>
                <td>{allData.chiSquareValue}</td>
              </tr>
              <tr>
                <th>Number of exams/reviews to complete without failure</th>
                <td>
                  <b>{allData.numberOfReviewToCompleteWithoutFailure}</b>
                </td>
              </tr>
            </tbody>
          </Table>
          <Heading heading="Achieved target calculator" />
          <Row className="mb-3">
            <Form.Group as={Col} md="4">
              <Form.Label>Number of reviews/exams completed</Form.Label>
              <Form.Control
                required
                type="number"
                placeholder="Reviews completed"
                defaultValue="0"
                onChange={(event) => setCompletedExams(event.target.value)}
              />
              <Form.Control.Feedback>Looks good!</Form.Control.Feedback>
            </Form.Group>

            <Form.Group as={Col} md="4">
              <Form.Label>Achieved target</Form.Label>
              <Form.Control
                required
                type="number"
                value={(allData.chiSquareValue * 1000) / (completedExams * 2)}
                disabled
              />
              <Form.Control.Feedback>Looks good!</Form.Control.Feedback>
            </Form.Group>
          </Row>
        </>
      ) : (
        <></>
      )}
    </div>
  );
};

export default ReliTarget;
