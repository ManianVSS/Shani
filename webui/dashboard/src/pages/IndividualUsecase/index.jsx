import React from "react";
import { useParams } from "react-router-dom";
import { Container, Col, Row, Table } from "react-bootstrap";
import { axiosClient } from "../../api/AxiosInstance";
const IndividualUsecase = (props) => {
  const [usecaseDetails, setUsecaseDetails] = React.useState({});
  const [attachmentids, setAttachmentids] = React.useState([]);
  const [attachmentDetailss, setAttachmentDetailss] = React.useState([]);

  const { usecaseid } = useParams();
  React.useEffect(() => {
    axiosClient.get("/requirements/api/use_cases/" + usecaseid + "/").then((response) => {
      setUsecaseDetails(response.data);
      setAttachmentids(response.data.attachments);

      response.data.attachments?.map((item) => {
        axiosClient.get("/requirements/api/attachments/" + item + "/").then((res) => {
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
                  <th>Usecase ID</th>
                </tr>
              </thead>
              <tbody
                style={{
                  border: "1px solid black",
                }}
              >
                <tr>
                  <td>{usecaseid}</td>
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
                  <th>Usecase Name</th>
                </tr>
              </thead>
              <tbody
                style={{
                  border: "1px solid black",
                }}
              >
                <tr>
                  <td>{usecaseDetails.name}</td>
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
                  <th>Usecase Weight</th>
                </tr>
              </thead>
              <tbody
                style={{
                  border: "1px solid black",
                }}
              >
                <tr>
                  <td>{usecaseDetails.weight}</td>
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
                  <th>Usecase Status</th>
                </tr>
              </thead>
              <tbody
                style={{
                  border: "1px solid black",
                }}
              >
                <tr>
                  <td>{usecaseDetails.status}</td>
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
                  <th>Usecase Consumer Score</th>
                </tr>
              </thead>
              <tbody
                style={{
                  border: "1px solid black",
                }}
              >
                <tr>
                  <td>{usecaseDetails.consumer_score}</td>
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
                  <th>Usecase Serviceability Score</th>
                </tr>
              </thead>
              <tbody
                style={{
                  border: "1px solid black",
                }}
              >
                <tr>
                  <td>{usecaseDetails.serviceability_score}</td>
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
                  <th>Usecase Test Confidence</th>
                </tr>
              </thead>
              <tbody
                style={{
                  border: "1px solid black",
                }}
              >
                <tr>
                  <td>{usecaseDetails.test_confidence}</td>
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
                  <th>Usecase Development Confidence</th>
                </tr>
              </thead>
              <tbody
                style={{
                  border: "1px solid black",
                }}
              >
                <tr>
                  <td>{usecaseDetails.development_confidence}</td>
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
                  <th>Usecase Category Details</th>
                </tr>
              </thead>
              <tbody
                style={{
                  border: "1px solid black",
                }}
              >
                <tr>
                  <td>{usecaseDetails.category}</td>
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
                  <td>{usecaseDetails.summary}</td>
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
                  <td>{usecaseDetails.description}</td>
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

export default IndividualUsecase;
