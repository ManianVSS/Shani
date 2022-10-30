import React, { useState, useEffect } from "react";
import { axiosClient } from "../../hooks/api";
import { Form, Col, Row, Container, Button, Table } from "react-bootstrap";
import { enGB } from "date-fns/locale";
import { DateRangePicker, START_DATE, END_DATE } from "react-nice-dates";
import "react-nice-dates/build/style.css";
import "./style.css";
import Heading from "../../components/Heading";

const EngineerAvailability = () => {
  const [startDate, setStartDate] = useState();
  const [endDate, setEndDate] = useState();
  const [show, setShow] = useState(false);
  const [engineerData, setEngineerData] = useState([]);
  const [engineer, setEngineer] = useState(null);
  const [engineerAvailabilityData, setEngineerAvailabilityData] = useState({});
  const showDetails = () => {
    axiosClient
      .get(
        "/engineer_capacity_view?engineer=" +
          engineer +
          "&from=" +
          formatDate(startDate) +
          "&to=" +
          formatDate(endDate),
        {
          headers: {
            authorization:
              "Bearer " + window.localStorage.getItem("accessToken"),
          },
        }
      )
      .then((response) => {
        setEngineerAvailabilityData(response.data);
      });
  };
  function formatDate(date) {
    var d = new Date(date),
      month = "" + (d.getMonth() + 1),
      day = "" + d.getDate(),
      year = d.getFullYear();

    if (month.length < 2) month = "0" + month;
    if (day.length < 2) day = "0" + day;

    return [year, month, day].join("-");
  }
  useEffect(() => {
    axiosClient.get("/engineers/").then((response) => {
      setEngineerData(response.data.results);
    });
  }, []);
  return (
    <div>
      <Heading heading={"ENGINEER AVAILABILITY VIEW"} />
      <Container>
        <Form>
          <Row className="mb-3">
            <Form.Group as={Col} controlId="formGridState">
              <Form.Label>ENGINEER</Form.Label>
              <Form.Select
                defaultValue="Choose..."
                onChange={(event) => setEngineer(event.target.value)}
              >
                <option>Choose...</option>
                {engineerData.map((item) => {
                  return (
                    <option value={item.id} key={item.id}>
                      {item.employee_id}
                    </option>
                  );
                })}
              </Form.Select>
            </Form.Group>
            <Form.Group as={Col} controlId="formGridState">
              <Form.Label>SELECT DATE RANGE</Form.Label>
              <DateRangePicker
                startDate={startDate}
                endDate={endDate}
                onStartDateChange={setStartDate}
                onEndDateChange={setEndDate}
                // minimumDate={new Date()}
                minimumLength={0}
                format="dd MMM yyyy"
                locale={enGB}
              >
                {({ startDateInputProps, endDateInputProps, focus }) => (
                  <div className="date-range">
                    <input
                      className={
                        "input" + (focus === START_DATE ? " -focused" : "")
                      }
                      {...startDateInputProps}
                      placeholder="Start date"
                    />
                    <span className="date-range_arrow" />
                    <input
                      className={
                        "input" + (focus === END_DATE ? " -focused" : "")
                      }
                      {...endDateInputProps}
                      placeholder="End date"
                    />
                  </div>
                )}
              </DateRangePicker>
            </Form.Group>
          </Row>
          <Button
            variant="primary"
            onClick={() => {
              setShow(true);
              showDetails();
            }}
          >
            Fetch Data
          </Button>
        </Form>
        {show ? (
          <>
            <Table bordered style={{ marginTop: "40px" }}>
              <thead>
                <tr>
                  <th>Engineer Name</th>
                  <th>Employee ID</th>
                  <th>Total Working Days</th>
                  <th>Leave Count</th>
                  <th>Site Holiday Count</th>
                  <th>Available Days</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>{engineerAvailabilityData["name"]}</td>
                  <td>{engineerAvailabilityData["employee_id"]}</td>
                  <td>{engineerAvailabilityData["work_days"]}</td>
                  <td>{engineerAvailabilityData["leave_count"]}</td>
                  <td>{engineerAvailabilityData["site_holiday_count"]}</td>
                  <td>{engineerAvailabilityData["available_days"]}</td>
                </tr>
              </tbody>
            </Table>
          </>
        ) : (
          <></>
        )}
      </Container>
    </div>
  );
};

export default EngineerAvailability;
