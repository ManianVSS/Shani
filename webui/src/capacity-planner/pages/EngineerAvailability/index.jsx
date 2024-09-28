import React, { useState, useEffect } from "react";
import { Form, Col, Row, Container, Button, Table } from "react-bootstrap";
import { enGB } from "date-fns/locale";
import { DateRangePicker, START_DATE, END_DATE } from "react-nice-dates";
import "react-nice-dates/build/style.css";
import "./style.css";
import Heading from "../../components/Heading";
import { useRecoilState } from "recoil";
import { authState } from "../../../state/authData";
import { axiosClientForCapacity } from "../../capacityApi";
import { useAlert } from "react-alert";

const EngineerAvailability = () => {
  const alert = useAlert();
  const [startDate, setStartDate] = useState(new Date());
  const [userData, setUserData] = useRecoilState(authState);
  const [endDate, setEndDate] = useState(new Date());
  const [show, setShow] = useState(false);
  const [engineerData, setEngineerData] = useState([]);
  const [engineer, setEngineer] = useState("Choose...");
  const [engineerAvailabilityData, setEngineerAvailabilityData] = useState({});
  const showDetails = () => {
    setShow(false);
    if (engineer !== "Choose...") {
      axiosClientForCapacity
        .get(
          "/people/api/engineer_capacity_view?engineer=" +
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
          setShow(true);
        });
    } else {
      alert.error("Please choose valid engineer");
    }
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
    axiosClientForCapacity
      .get("/people/api/engineers/", {
        headers: {
          authorization: "Bearer " + window.localStorage.getItem("accessToken"),
        },
      })
      .then((response) => {
        setEngineerData(response.data.results);
      });
    setUserData({
      accessToken: window.localStorage.getItem("accessToken"),
      authStatus: true,
      errorMessage: "",
      userName: window.localStorage.getItem("user"),
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
            style={{ background: "#404040", color: "white" }}
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
            <Table
              bordered
              className={
                window.localStorage.getItem("testCenterTheme") === "dark"
                  ? "dark-table"
                  : "light-table"
              }
            >
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
