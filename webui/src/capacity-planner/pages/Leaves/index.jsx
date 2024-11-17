import React, { useState, useEffect } from "react";
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
import { useRecoilValue, useRecoilState } from "recoil";
import { authState } from "../../../state/authData";
import { useAlert } from "react-alert";
import { axiosClientForCapacity } from "../../capacityApi";

const Leaves = () => {
  const alert = useAlert();
  const [startDate, setStartDate] = useState(new Date());
  const [endDate, setEndDate] = useState(new Date());
  const [startLeaveDate, setStartLeaveDate] = useState(new Date());
  const [endLeaveDate, setEndLeaveDate] = useState(new Date());
  const [show, setShow] = useState(false);
  const [userData, setUserData] = useRecoilState(authState);
  const [engineerData, setEngineerData] = useState([]);
  const [engineer, setEngineer] = useState("Choose...");
  const [engineerName, setEngineerName] = useState(null);
  const [engineerAvailabilityData, setEngineerAvailabilityData] = useState([]);
  const [showModal, setShowModal] = useState(false);
  const [summary, setSummary] = useState("");

  const handleClose = () => setShowModal(false);
  const handleShow = () => setShowModal(true);
  const showDetails = () => {
    setShow(false);
    if (engineer !== "Choose...") {
      axiosClientForCapacity
        .get(
          "/people/api/leaves/?engineer=" +
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
          setShow(true);
        });
    } else {
      alert.error("Please choose valid engineer to load the data");
    }
  };
  // const showAllLeaveDetails = () => {
  //   axiosClient
  //     .get("/leaves/?engineer=" + window.localStorage.getItem("userid"), {
  //       headers: {
  //         authorization: "Bearer " + window.localStorage.getItem("accessToken"),
  //       },
  //     })
  //     .then((response) => {
  //       setEngineerAvailabilityData(response.data.results);
  //     });
  // };

  const applyLeave = () => {
    axiosClientForCapacity
      .post(
        "/people/api/leaves/",
        {
          engineer: window.localStorage.getItem("userid"),
          start_date: formatDate(startLeaveDate),
          end_date: formatDate(endLeaveDate),
          summary: summary,
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
        alert.succes("Leave Applied");
        showDetails();
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

  const leaveData = engineerAvailabilityData.map((item) => {
    return (
      <tr key={item.id}>
        <td>{engineerName}</td>
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
                <Form.Control
                  type="text"
                  placeholder="Summary"
                  onChange={(event) => setSummary(event.target.value)}
                />
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
          <Button
            variant="secondary"
            style={{ background: "#404040", color: "white" }}
            onClick={handleClose}
          >
            Cancel
          </Button>
          <Button
            variant="primary"
            style={{ background: "#404040", color: "white" }}
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
      <Button
        variant="success"
        style={{ marginLeft: "75%", background: "#404040", color: "white" }}
        onClick={handleShow}
      >
        +
      </Button>
      <Container>
        <Form>
          <Row className="mb-3">
            <Form.Group as={Col} controlId="formGridState">
              <Form.Label>ENGINEER</Form.Label>
              <Form.Select
                defaultValue="Choose..."
                onChange={(event) => {
                  setShow(false);
                  setEngineer(event.target.value.split("_")[0]);
                  setEngineerName(event.target.value.split("_")[1]);
                }}
              >
                <option>Choose...</option>
                {engineerData.map((item) => {
                  return (
                    <option
                      value={item.id + "_" + item.employee_id}
                      key={item.id}
                    >
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
          <div className="leave-buttons">
            <Button
              style={{ background: "#404040", color: "white" }}
              variant="primary"
              onClick={() => {
                setShow(true);
                showDetails();
              }}
            >
              Fetch Data
            </Button>
          </div>
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
