import React from "react";
import { useParams } from "react-router-dom";
import { Container, Col, Row, Table } from "react-bootstrap";
import { axiosClientBasic } from "../../../hooks/api";

const IndividualReqComponent = (props) => {
  const { requirementid } = useParams();
  const [reqDetails, setReqDetails] = React.useState({});
  const [attachmentids, setAttachmentids] = React.useState([]);
  const [attachmentDetailss, setAttachmentDetailss] = React.useState([]);
  React.useEffect(() => {
    axiosClientBasic
      .get("/requirements/api/requirements/" + requirementid + "/", {
        headers: {
          authorization: "Bearer " + window.localStorage.getItem("accessToken"),
        },
      })
      .then((response) => {
        setReqDetails(response.data);
        setAttachmentids(response.data.attachments);

        response.data.attachments?.map((item) => {
          axiosClientBasic
            .get("/requirements/api/attachments/" + item + "/", {
              headers: {
                authorization:
                  "Bearer " + window.localStorage.getItem("accessToken"),
              },
            })
            .then((res) => {
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
                  <th>Requirement ID</th>
                </tr>
              </thead>
              <tbody
                style={{
                  border: "1px solid black",
                }}
              >
                <tr>
                  <td>{requirementid}</td>
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
                  <th>Requirement Name</th>
                </tr>
              </thead>
              <tbody
                style={{
                  border: "1px solid black",
                }}
              >
                <tr>
                  <td>{reqDetails.name}</td>
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
                  <th>Requirement Cost</th>
                </tr>
              </thead>
              <tbody
                style={{
                  border: "1px solid black",
                }}
              >
                <tr>
                  <td>{reqDetails.cost}</td>
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
                  <td>{reqDetails.summary}</td>
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
                  <td>{reqDetails.description}</td>
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

export default IndividualReqComponent;
