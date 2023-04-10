import React, { useState, useEffect } from "react";
import { axiosClient } from "../../hooks/api";
import { Form, Col, Row, Container, Button, Table } from "react-bootstrap";
import { enGB } from "date-fns/locale";
import { DateRangePicker, START_DATE, END_DATE } from "react-nice-dates";
import "react-nice-dates/build/style.css";
import "./style.css";
import Heading from "../../components/Heading";
import OverlayTrigger from "react-bootstrap/OverlayTrigger";
import Tooltip from "react-bootstrap/Tooltip";
import { useRecoilState } from "recoil";
import { authState } from "../../state/authData";

const Capacity = () => {
  const [userData, setUserData] = useRecoilState(authState);
  const [startDate, setStartDate] = useState();
  const [endDate, setEndDate] = useState();
  const [show, setShow] = useState(false);
  const [orgData, setOrgData] = useState([]);
  const [org, setOrg] = useState(null);
  const [capacityData, setCapacityData] = useState({});
  const showDetails = () => {
    axiosClient
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
      });
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
  useEffect(() => {
    axiosClient.get("/api/org_groups/").then((response) => {
      setOrgData(response.data.results);
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
            <Form.Group as={Col} controlId="formGridState">
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
          </Row>
          <Button
            variant="primary"
            onClick={() => {
              if (org !== "Choose...") {
                setShow(true);
                showDetails();
              } else {
                setShow(false);
              }
            }}
          >
            Fetch Data
          </Button>
        </Form>
        {show ? (
          <>
            <Table bordered size="sm" style={{ marginTop: "40px" }}>
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
            <Table bordered style={{ marginTop: "40px" }}>
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
