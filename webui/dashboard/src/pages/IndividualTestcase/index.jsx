import React from "react";
import { useParams } from "react-router-dom";
import { Container, Col, Row, Table } from "react-bootstrap";
import { axiosClient } from "../../api/AxiosInstance";
const IndividualTestcase = (props) => {
  const [testCaseDetails, setTestCaseDetails] = React.useState({});
  const [attachmentids, setAttachmentids] = React.useState([]);
  const [attachmentDetailss, setAttachmentDetailss] = React.useState([]);

  const { testcaseid } = useParams();
  React.useEffect(() => {
    axiosClient.get("/testdesign/api/testcases/" + testcaseid + "/").then((response) => {
      setTestCaseDetails(response.data);
      setAttachmentids(response.data.attachments);

      response.data.attachments?.map((item) => {
        axiosClient.get("/testdesign/api/attachments/" + item + "/").then((res) => {
          setAttachmentDetailss((oldArray) => [
            ...oldArray,
            {
              name: res.data.name,
              file: res.data.file,
            },
          ]);
        });
      });
    });
  }, []);
  return (
    <>
      <Container>
        <Row>
          <Col sm>
            <Table striped bordered hover>
              <thead
                style={{
                  color: "white",
                  background: "gray",
                  fontWeight: "bold",
                  border: "1px solid black",
                }}
              >
                <tr>
                  <th>Testcase ID</th>
                </tr>
              </thead>
              <tbody
                style={{
                  border: "1px solid black",
                }}
              >
                <tr>
                  <td>{testcaseid}</td>
                </tr>
              </tbody>
            </Table>
          </Col>
          <Col sm>
            <Table striped bordered hover>
              <thead
                style={{
                  color: "white",
                  background: "gray",
                  fontWeight: "bold",
                  border: "1px solid black",
                }}
              >
                <tr>
                  <th>Testcase Name</th>
                </tr>
              </thead>
              <tbody
                style={{
                  border: "1px solid black",
                }}
              >
                <tr>
                  <td>{testCaseDetails.name}</td>
                </tr>
              </tbody>
            </Table>
          </Col>
          <Col sm>
            <Table striped bordered hover>
              <thead
                style={{
                  color: "white",
                  background: "gray",
                  fontWeight: "bold",
                  border: "1px solid black",
                }}
              >
                <tr>
                  <th>TestCase Status</th>
                </tr>
              </thead>
              <tbody
                style={{
                  border: "1px solid black",
                }}
              >
                <tr>
                  <td>{testCaseDetails.status}</td>
                </tr>
              </tbody>
            </Table>
          </Col>
        </Row>
        <Row>
          <Col sm>
            <Table striped bordered hover>
              <thead
                style={{
                  color: "white",
                  background: "gray",
                  fontWeight: "bold",
                  border: "1px solid black",
                }}
              >
                <tr>
                  <th>Is this an Acceptance Test?</th>
                </tr>
              </thead>
              <tbody
                style={{
                  border: "1px solid black",
                }}
              >
                <tr>
                  <td>{testCaseDetails.acceptance_test}</td>
                </tr>
              </tbody>
            </Table>
          </Col>
          <Col sm>
            <Table striped bordered hover>
              <thead
                style={{
                  color: "white",
                  background: "gray",
                  fontWeight: "bold",
                  border: "1px solid black",
                }}
              >
                <tr>
                  <th>Is this test Automated?</th>
                </tr>
              </thead>
              <tbody
                style={{
                  border: "1px solid black",
                }}
              >
                <tr>
                  <td>{testCaseDetails.automated}</td>
                </tr>
              </tbody>
            </Table>
          </Col>
          <Col sm>
            <Table striped bordered hover>
              <thead
                style={{
                  color: "white",
                  background: "gray",
                  fontWeight: "bold",
                  border: "1px solid black",
                }}
              >
                <tr>
                  <th>Usecase ID</th>
                </tr>
              </thead>
              <tbody
                style={{
                  border: "1px solid black",
                }}
              >
                <tr>
                  <td>{testCaseDetails.use_case}</td>
                </tr>
              </tbody>
            </Table>
          </Col>
        </Row>
        <Row>
          <Col>
            <Table striped bordered hover>
              <thead
                style={{
                  color: "white",
                  background: "gray",
                  fontWeight: "bold",
                  border: "1px solid black",
                }}
              >
                <tr>
                  <th>Summary</th>
                </tr>
              </thead>
              <tbody
                style={{
                  border: "1px solid black",
                }}
              >
                <tr>
                  <td>{testCaseDetails.summary}</td>
                </tr>
              </tbody>
            </Table>
          </Col>
        </Row>
        <Row>
          <Col>
            <Table striped bordered hover>
              <thead
                style={{
                  color: "white",
                  background: "gray",
                  fontWeight: "bold",
                  border: "1px solid black",
                }}
              >
                <tr>
                  <th>Description</th>
                </tr>
              </thead>
              <tbody
                style={{
                  border: "1px solid black",
                }}
              >
                <tr>
                  <td>{testCaseDetails.description}</td>
                </tr>
              </tbody>
            </Table>
          </Col>
        </Row>
        <Row>
          <Col>
            <Table striped bordered hover>
              <thead
                style={{
                  color: "white",
                  background: "gray",
                  fontWeight: "bold",
                  border: "1px solid black",
                }}
              >
                <tr>
                  <th>Attachments</th>
                </tr>
              </thead>
              <tbody
                style={{
                  border: "1px solid black",
                }}
              >
                <tr>
                  <td>
                    {attachmentDetailss.map((item) => {
                      return (
                        <a
                          download={item.name}
                          href={item.file}
                          style={{
                            border: "1px solid black",
                            padding: "3px",
                            margin: "3px",
                            textDecoration: "none",
                            color: "black",
                            borderRadius: "15px",
                            cursor: "pointer",
                          }}
                        >
                          {item.name}
                        </a>
                      );
                    })}
                  </td>
                </tr>
              </tbody>
            </Table>
          </Col>
        </Row>
      </Container>
    </>
  );
};

export default IndividualTestcase;
