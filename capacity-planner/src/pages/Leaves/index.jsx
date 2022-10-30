import React, { useState, useEffect } from "react";
import { axiosClient } from "../../hooks/api";
import {
  Form,
  Col,
  Row,
  Container,
  Button,
  Table,
  Modal,
} from "react-bootstrap";
import { enGB } from "date-fns/locale";
import { DateRangePicker, START_DATE, END_DATE } from "react-nice-dates";
import "react-nice-dates/build/style.css";
import "./style.css";
import Heading from "../../components/Heading";
import { useRecoilValue } from "recoil";
import { authState } from "../../state/authData";

const Leaves = () => {
  const [startDate, setStartDate] = useState();
  const [endDate, setEndDate] = useState();
  const [startLeaveDate, setStartLeaveDate] = useState();
  const [endLeaveDate, setEndLeaveDate] = useState();
  const [show, setShow] = useState(false);
  const [engineerData, setEngineerData] = useState([]);
  const [engineer, setEngineer] = useState(null);
  const [engineerAvailabilityData, setEngineerAvailabilityData] = useState([]);
  const [showModal, setShowModal] = useState(false);
  const userData = useRecoilValue(authState);
  const handleClose = () => setShowModal(false);
  const handleShow = () => setShowModal(true);
  const showDetails = () => {
    axiosClient
      .get(
        "/leaves/?engineer=" +
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
        setEngineerAvailabilityData(response.data.results);
      });
  };
  console.log("====================================");
  console.log(userData);
  console.log("====================================");
  const applyLeave = () => {
    axiosClient
      .post(
        "/leaves/",
        {
          engineer: userData.userName,
          start_date: formatDate(startLeaveDate),
          end_date: formatDate(endLeaveDate),
          summary: "string",
          status: "DRAFT",
        },
        {
          headers: {
            authorization:
              "Bearer " + window.localStorage.getItem("accessToken"),
          },
        }
      )
      .then((response) => {
        setEngineerAvailabilityData(response.data.results);
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
  const leaveData = engineerAvailabilityData.map((item) => {
    return (
      <tr key={item.id}>
        <td>{item["name"]}</td>
        <td>{item["summary"]}</td>
        <td>{item["status"]}</td>
        <td>{item["start_date"]}</td>
        <td>{item["end_date"]}</td>
      </tr>
    );
  });
  return (
    <div>
      <Modal show={showModal} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Apply Leave</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form>
            <Row className="mb-3">
              <Form.Group as={Col} controlId="formGridEmail">
                <Form.Label>Summary</Form.Label>
                <Form.Control type="text" placeholder="Summary" />
              </Form.Group>

              <Form.Group as={Col} controlId="formGridState">
                <Form.Label>SELECT DATE RANGE</Form.Label>
                <DateRangePicker
                  startDate={startLeaveDate}
                  endDate={endLeaveDate}
                  onStartDateChange={setStartLeaveDate}
                  onEndDateChange={setEndLeaveDate}
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
          </Form>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Cancel
          </Button>
          <Button
            variant="primary"
            onClick={() => {
              handleClose();
              applyLeave();
            }}
          >
            Apply
          </Button>
        </Modal.Footer>
      </Modal>
      <Heading heading={"LEAVES DATA"} />
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
          <div className="leave-buttons">
            <Button
              variant="primary"
              onClick={() => {
                setShow(true);
                showDetails();
              }}
            >
              Fetch Data
            </Button>
            <Button
              variant="success"
              style={{ marginLeft: "75%" }}
              onClick={handleShow}
            >
              Apply Leave
            </Button>
          </div>
        </Form>
        {show ? (
          <>
            <Table bordered style={{ marginTop: "40px" }}>
              <thead>
                <tr>
                  <th>Engineer Name</th>
                  <th>Summary</th>
                  <th>Leave status</th>
                  <th>Start Date</th>
                  <th>End Date</th>
                </tr>
              </thead>
              <tbody>{leaveData}</tbody>
            </Table>
          </>
        ) : (
          <></>
        )}
      </Container>
    </div>
  );
};

export default Leaves;
