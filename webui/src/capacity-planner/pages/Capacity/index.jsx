import React, { useState, useEffect } from "react";

import { Form, Col, Row, Container, Button, Table } from "react-bootstrap";
import { enGB } from "date-fns/locale";
import { DateRangePicker, START_DATE, END_DATE } from "react-nice-dates";
import "react-nice-dates/build/style.css";
import "./style.css";
import Heading from "../../components/Heading";
import OverlayTrigger from "react-bootstrap/OverlayTrigger";
import Tooltip from "react-bootstrap/Tooltip";
import { useRecoilState } from "recoil";
import { authState } from "../../../state/authData";
import { axiosClientForCapacity, axiosClientForLogin } from "../../capacityApi";
import { useAlert } from "react-alert";

const Capacity = () => {
  const alert = useAlert();
  const [userData, setUserData] = useRecoilState(authState);
  const [startDate, setStartDate] = useState(new Date());
  const [endDate, setEndDate] = useState(new Date());
  const [show, setShow] = useState(false);
  const [orgData, setOrgData] = useState([]);
  const [sprintData, setSprintData] = useState([]);
  const [org, setOrg] = useState("Choose...");
  const [sprint, setSprint] = useState("Choose...");
  const [capacityData, setCapacityData] = useState({});
  const showDetails = () => {
    setShow(false);
    if (org !== "Choose...") {
      axiosClientForCapacity
        .get(
          "/people/api/capacity_view?org_group=" +
            org +
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
          setCapacityData(response.data);
          setShow(true);
        });
    } else {
      alert.error("Please choose valid Org Group");
    }
  };
  const rows = [];
  for (const key in capacityData["engineer_data"]) {
    rows.push(
      <tr key={key}>
        <td>{capacityData["engineer_data"][key]["name"]}</td>
        <td>{capacityData["engineer_data"][key]["available_days"]}</td>
        <td>{capacityData["engineer_data"][key]["capacity"].toFixed(2)}</td>
        <td>{capacityData["engineer_data"][key]["employee_id"]}</td>
        <td>
          <OverlayTrigger
            placement="top"
            delay={{ show: 200, hide: 400 }}
            overlay={
              <Tooltip id="button-tooltip">
                {capacityData["engineer_data"][key]["leave_plans"].map(
                  (item) => {
                    return (
                      <p key={item.start_date}>
                        Start-{item.start_date} to End-{item.end_date}
                      </p>
                    );
                  }
                )}
              </Tooltip>
            }
          >
            <p>{capacityData["engineer_data"][key]["leave_count"]}</p>
          </OverlayTrigger>
        </td>
        <td>{capacityData["engineer_data"][key]["participation_capacity"]}</td>
        <td>
          <OverlayTrigger
            placement="top"
            delay={{ show: 200, hide: 400 }}
            overlay={
              <Tooltip id="button-tooltip">
                {capacityData["engineer_data"][key]["site_holidays"].map(
                  (item) => {
                    return (
                      <p key={item.name}>
                        {item.name} : {item.date}
                      </p>
                    );
                  }
                )}
              </Tooltip>
            }
          >
            <p>{capacityData["engineer_data"][key]["site_holiday_count"]}</p>
          </OverlayTrigger>
        </td>
      </tr>
    );
  }
  const setDatesForSelectedSprint = (sprintID) => {
    if (sprintID !== "Choose...") {
      axiosClientForCapacity
        .get(`/workitems/api/sprints/${sprintID}`, {
          headers: {
            authorization:
              "Bearer " + window.localStorage.getItem("accessToken"),
          },
        })
        .then((response) => {
          console.log(new Date(response.data.start_date));
          console.log(new Date(response.data.end_date));
          console.log(startDate + "-" + endDate);
          setStartDate(new Date(response.data.start_date));
          setEndDate(new Date(response.data.end_date));
        });
    }
  };
  useEffect(() => {
    axiosClientForLogin
      .get("/org_groups/", {
        headers: {
          authorization: "Bearer " + window.localStorage.getItem("accessToken"),
        },
      })
      .then((response) => {
        setOrgData(response.data.results);
      });
    axiosClientForCapacity
      .get("/workitems/api/sprints/", {
        headers: {
          authorization: "Bearer " + window.localStorage.getItem("accessToken"),
        },
      })
      .then((response) => {
        setSprintData(response.data.results);
      });
    setUserData({
      accessToken: window.localStorage.getItem("accessToken"),
      authStatus: true,
      errorMessage: "",
      userName: window.localStorage.getItem("user"),
    });
  }, []);

  function formatDate(date) {
    var d = new Date(date),
      month = "" + (d.getMonth() + 1),
      day = "" + d.getDate(),
      year = d.getFullYear();

    if (month.length < 2) month = "0" + month;
    if (day.length < 2) day = "0" + day;

    return [year, month, day].join("-");
  }

  return (
    <div>
      <Heading heading={"CAPACITY VIEW"} />
      <Container>
        <Form>
          <Row className="mb-3">
            <Form.Group as={Row} controlId="formGridState">
              <Form.Label>ORG GROUP</Form.Label>
              <Form.Select
                defaultValue="Choose..."
                onChange={(event) => setOrg(event.target.value)}
              >
                <option>Choose...</option>
                {orgData.map((item) => {
                  return (
                    <option value={item.id} key={item.id}>
                      {item.name}
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
            <Form.Group as={Col} controlId="formGridState">
              <Form.Label>SPRINT</Form.Label>
              <Form.Select
                defaultValue="Choose..."
                onChange={(event) => {
                  // setSprint(event.target.value);
                  setDatesForSelectedSprint(event.target.value);
                }}
              >
                <option>Choose...</option>
                {sprintData.map((item) => {
                  return (
                    <option value={item.id} key={item.id}>
                      PI-{item.pi}-{item.number}
                    </option>
                  );
                })}
              </Form.Select>
            </Form.Group>
          </Row>
          <Button
            variant="info"
            style={{ background: "#404040", color: "white" }}
            onClick={() => {
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
              size="sm"
              className={
                window.localStorage.getItem("testCenterTheme") === "dark"
                  ? "dark-table"
                  : "light-table"
              }
            >
              <tbody>
                <tr>
                  <td>Total Work Days</td>
                  <td>{capacityData.work_days}</td>
                </tr>
                <tr>
                  <td>Total Org Group Capacity(in Person days)</td>
                  <td>{capacityData.total_capacity?.toFixed(2)}</td>
                </tr>
              </tbody>
            </Table>
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
                  <th>Available Days</th>
                  <th>Capacity</th>
                  <th>Employee ID</th>
                  <th>Leave Count</th>
                  <th>Participation Capacity</th>
                  <th>Site Holiday Count</th>
                </tr>
              </thead>
              <tbody>{rows}</tbody>
            </Table>
          </>
        ) : (
          <></>
        )}
      </Container>
    </div>
  );
};

export default Capacity;
