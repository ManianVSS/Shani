import React, { useEffect, useState } from "react";
import { useWindowSize } from "../../hooks/windowSize";
import { axiosClient, axiosClientBasic } from "../../hooks/api";
import { Button, Col, Container, Form, Row, Table } from "react-bootstrap";
import "./style.css";
import { useRecoilValue } from "recoil";
import { colorScheme } from "../../state/mode";

const data = [
  {
    id: 1,
    name: "Server001",
    properties: {
      serverIP: "10.13.13.13",
    },
    commands: {
      command1: "This is command 1",
    },
  },
  {
    id: 2,
    name: "VM001",
    properties: {
      VMIP: "10.13.13.13",
    },
    commands: {
      shutDownVM: "This is VM shut down command",
    },
  },
  {
    id: 3,
    name: "DC001",
    properties: {
      DCIP: "10.13.13.13",
    },
    commands: {
      DCRestart: "This is DC restart command",
    },
  },
];
const Invoker = () => {
  const mode = useRecoilValue(colorScheme);
  const { height } = useWindowSize();
  const [allEnvDetails, setAllEnvDetails] = useState([]);
  const [selectedEnv, setSelectedEnv] = useState(allEnvDetails[0]);
  const handleSelectChange = (event) => {
    axiosClientBasic
      .get("/execution/api/environments/" + event.target.value, {
        headers: {
          authorization: "Bearer " + window.localStorage.getItem("accessToken"),
        },
      })
      .then((response) => {
        setSelectedEnv(response.data);
      });
  };
  const getAllEnvData = () => {
    axiosClientBasic
      .get("/execution/api/environments/", {
        headers: {
          authorization: "Bearer " + window.localStorage.getItem("accessToken"),
        },
      })
      .then((response) => {
        setAllEnvDetails(response.data.results);
      });
  };

  useEffect(() => {
    getAllEnvData();
  }, []);

  useEffect(() => {
    setSelectedEnv(allEnvDetails[0]);
  }, [allEnvDetails]);

  console.log(allEnvDetails);
  console.log(selectedEnv);
  return (
    <div>
      <Container>
        <Form.Select
          aria-label="Environment Selectbox"
          //   value={allEnvDetails.id}
          onChange={handleSelectChange}
        >
          {allEnvDetails?.map((item, index) => {
            return (
              <option value={item.id} key={index}>
                {item.name}
              </option>
            );
          })}
        </Form.Select>
      </Container>
      <Row className="justify-content-md-center" style={{ margin: "10px" }}>
        <Col
          sm={8}
          className="borderWithRadius textAlignCenter"
          style={{ height: height * 0.8 }}
        >
          <h2 className="h2Style">Properties</h2>

          {Object.keys(selectedEnv ?? {}).length === 0 ? (
            <>Please select on environment</>
          ) : (
            <Table striped bordered hover>
              <tbody>
                {Object.keys(selectedEnv?.properties).map((item, index) => {
                  return (
                    <tr key={index}>
                      <th>{item}</th>
                      <td>{selectedEnv.properties[item]}</td>
                    </tr>
                  );
                })}
              </tbody>
            </Table>
          )}
        </Col>
        <Col
          sm={4}
          className="borderWithRadius textAlignCenter"
          style={{ height: height * 0.8 }}
        >
          <h2 className="h2Style">Commands</h2>
          <Container>
            {Object.keys(selectedEnv ?? {}).length === 0 ? (
              <>Please select on environment</>
            ) : (
              <Row>
                {Object.keys(selectedEnv?.properties).map((item, index) => {
                  return (
                    <Col key={index}>
                      <Button
                        key={index}
                        onClick={() => {
                          console.log(selectedEnv?.commands[item]);
                        }}
                        style={{
                          margin: "5px",
                          color: mode === "light" ? "black" : "white",
                        }}
                      >
                        {item}
                      </Button>
                    </Col>
                  );
                })}
              </Row>
            )}
          </Container>
        </Col>
      </Row>
    </div>
  );
};

export default Invoker;
