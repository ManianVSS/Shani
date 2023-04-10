import React from "react";
import { useParams } from "react-router-dom";
import { Container, Col, Row, Table } from "react-bootstrap";
import { axiosClient } from "../../api/AxiosInstance";
const IndividualFeature = (props) => {
  const [featureDetails, setFeatureDetails] = React.useState({});
  const [attachmentids, setAttachmentids] = React.useState([]);
  const [attachmentDetailss, setAttachmentDetailss] = React.useState([]);

  const { usecasecategoryid } = useParams();
  React.useEffect(() => {
    axiosClient
      .get("/requirements/api/use_case_categories/" + usecasecategoryid + "/")
      .then((response) => {
        setFeatureDetails(response.data);
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
                  <th>Usecase Category ID</th>
                </tr>
              </thead>
              <tbody
                style={{
                  border: "1px solid black",
                }}
              >
                <tr>
                  <td>{usecasecategoryid}</td>
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
                  <th>Usecase Category Name</th>
                </tr>
              </thead>
              <tbody
                style={{
                  border: "1px solid black",
                }}
              >
                <tr>
                  <td>{featureDetails.name}</td>
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
                  <th>Usecase Category Weight</th>
                </tr>
              </thead>
              <tbody
                style={{
                  border: "1px solid black",
                }}
              >
                <tr>
                  <td>{featureDetails.weight}</td>
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
                  <td>{featureDetails.summary}</td>
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
                  <td>{featureDetails.description}</td>
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

export default IndividualFeature;
