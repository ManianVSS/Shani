import React, { useEffect, useState } from "react";
import {
  MDBCol,
  MDBContainer,
  MDBRow,
  MDBCard,
  MDBCardText,
  MDBCardBody,
  MDBCardImage,
  MDBBtn,
  MDBBreadcrumb,
  MDBBreadcrumbItem,
  MDBProgress,
  MDBProgressBar,
  MDBIcon,
  MDBListGroup,
  MDBListGroupItem,
} from "mdb-react-ui-kit";
import { GiAlliedStar } from "react-icons/gi";
import { Card, ListGroup } from "react-bootstrap";
import { axiosClientForCapacity } from "../../capacity-planner/capacityApi";

const Profile = () => {
  const [userDetails, setUserDetails] = useState({});
  const getUserDetails = () => {
    axiosClientForCapacity
      .get("/engineers/1/", {
        headers: {
          authorization: "Bearer " + window.localStorage.getItem("accessToken"),
        },
      })
      .then((res) => {
        setUserDetails(res.data);
      });
  };
  useEffect(() => {
    getUserDetails();
  }, []);

  return (
    <section style={{ backgroundColor: "#eee" }}>
      <MDBContainer className="py-5">
        <MDBRow>
          <MDBCol>
            <MDBBreadcrumb className="bg-light rounded-3 mb-4 p-3">
              <MDBBreadcrumbItem
                active
                style={{ fontWeight: "bold", margin: "auto", fontSize: "25px" }}
              >
                User Profile
              </MDBBreadcrumbItem>
            </MDBBreadcrumb>
          </MDBCol>
        </MDBRow>

        <MDBRow>
          <MDBCol lg="4">
            <MDBCard className="mb-4">
              <MDBCardBody className="text-center">
                <MDBCardImage
                  src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava6.webp"
                  alt="avatar"
                  className="rounded-circle"
                  style={{
                    width: "150px",
                    margin: "auto",
                  }}
                  fluid
                />
                <p className="text-muted mb-1">{userDetails.role}</p>
                <p className="text-muted mb-4">Address, Address, IN</p>
                <div className="d-flex justify-content-center mb-2">
                  <MDBBtn>Follow</MDBBtn>
                  <MDBBtn outline className="ms-1">
                    Message
                  </MDBBtn>
                </div>
                <Card style={{ width: "50%", margin: "auto" }}>
                  <Card.Header style={{ fontWeight: "bold" }}>
                    Points Earned
                  </Card.Header>
                  <ListGroup variant="flush">
                    <ListGroup.Item>
                      <div className="grid-container-element">
                        <div
                          className="grid-child-element"
                          style={{ color: "#e6b800", fontWeight: "bold" }}
                        >
                          {userDetails.points}
                        </div>
                        <div className="grid-child-element">
                          <GiAlliedStar
                            style={{ marginTop: "4px", color: "#e6b800" }}
                          />
                        </div>
                      </div>
                    </ListGroup.Item>
                  </ListGroup>
                </Card>
              </MDBCardBody>
            </MDBCard>

            <MDBCard className="mb-lg-0 mb-4">
              <MDBCardBody className="p-0">
                <MDBListGroup flush className="rounded-3">
                  <MDBListGroupItem className="d-flex justify-content-between align-items-center p-3">
                    <MDBIcon fas icon="globe fa-lg text-warning" />
                    <MDBCardText>https://testportal.com</MDBCardText>
                  </MDBListGroupItem>
                  <MDBListGroupItem className="d-flex justify-content-between align-items-center p-3">
                    <MDBIcon
                      fab
                      icon="github fa-lg"
                      style={{ color: "#333333" }}
                    />
                    <MDBCardText>testportal</MDBCardText>
                  </MDBListGroupItem>
                  <MDBListGroupItem className="d-flex justify-content-between align-items-center p-3">
                    <MDBIcon
                      fab
                      icon="twitter fa-lg"
                      style={{ color: "#55acee" }}
                    />
                    <MDBCardText>@testportal</MDBCardText>
                  </MDBListGroupItem>
                  <MDBListGroupItem className="d-flex justify-content-between align-items-center p-3">
                    <MDBIcon
                      fab
                      icon="instagram fa-lg"
                      style={{ color: "#ac2bac" }}
                    />
                    <MDBCardText>testportal</MDBCardText>
                  </MDBListGroupItem>
                  <MDBListGroupItem className="d-flex justify-content-between align-items-center p-3">
                    <MDBIcon
                      fab
                      icon="facebook fa-lg"
                      style={{ color: "#3b5998" }}
                    />
                    <MDBCardText>testportal</MDBCardText>
                  </MDBListGroupItem>
                </MDBListGroup>
              </MDBCardBody>
            </MDBCard>
          </MDBCol>
          <MDBCol lg="8">
            <MDBCard className="mb-4">
              <MDBCardBody>
                <MDBRow>
                  <MDBCol sm="3">
                    <MDBCardText>Full Name</MDBCardText>
                  </MDBCol>
                  <MDBCol sm="9">
                    <MDBCardText className="text-muted">
                      {userDetails.name}
                    </MDBCardText>
                  </MDBCol>
                </MDBRow>
                <hr />
                <MDBRow>
                  <MDBCol sm="3">
                    <MDBCardText>Email</MDBCardText>
                  </MDBCol>
                  <MDBCol sm="9">
                    <MDBCardText className="text-muted">
                      example@example.com
                    </MDBCardText>
                  </MDBCol>
                </MDBRow>
                <hr />
                <MDBRow>
                  <MDBCol sm="3">
                    <MDBCardText>Phone</MDBCardText>
                  </MDBCol>
                  <MDBCol sm="9">
                    <MDBCardText className="text-muted">
                      (000) 000-0000
                    </MDBCardText>
                  </MDBCol>
                </MDBRow>
                <hr />
                <MDBRow>
                  <MDBCol sm="3">
                    <MDBCardText>Mobile</MDBCardText>
                  </MDBCol>
                  <MDBCol sm="9">
                    <MDBCardText className="text-muted">
                      (000) 000-0000
                    </MDBCardText>
                  </MDBCol>
                </MDBRow>
                <hr />
                <MDBRow>
                  <MDBCol sm="3">
                    <MDBCardText>Address</MDBCardText>
                  </MDBCol>
                  <MDBCol sm="9">
                    <MDBCardText className="text-muted">
                      Address, Address, IN
                    </MDBCardText>
                  </MDBCol>
                </MDBRow>
              </MDBCardBody>
            </MDBCard>

            <MDBRow>
              <MDBCol md="6">
                <MDBCard className="mb-md-0 mb-4">
                  <MDBCardBody>
                    <MDBCardText
                      className="mb-4"
                      style={{ fontWeight: "bold" }}
                    >
                      {/* <span className="text-primary font-italic me-1">
                        assigment
                      </span>{" "} */}
                      Skills
                    </MDBCardText>
                    <MDBCardText
                      className="mb-1"
                      style={{ fontSize: ".77rem" }}
                    >
                      Web Design
                    </MDBCardText>
                    <MDBProgress className="rounded">
                      <MDBProgressBar width={80} valuemin={0} valuemax={100} />
                    </MDBProgress>

                    <MDBCardText
                      className="mb-1 mt-4"
                      style={{ fontSize: ".77rem" }}
                    >
                      Website Markup
                    </MDBCardText>
                    <MDBProgress className="rounded">
                      <MDBProgressBar width={72} valuemin={0} valuemax={100} />
                    </MDBProgress>

                    <MDBCardText
                      className="mb-1 mt-4"
                      style={{ fontSize: ".77rem" }}
                    >
                      One Page
                    </MDBCardText>
                    <MDBProgress className="rounded">
                      <MDBProgressBar width={89} valuemin={0} valuemax={100} />
                    </MDBProgress>

                    <MDBCardText
                      className="mb-1 mt-4"
                      style={{ fontSize: ".77rem" }}
                    >
                      Mobile Template
                    </MDBCardText>
                    <MDBProgress className="rounded">
                      <MDBProgressBar width={55} valuemin={0} valuemax={100} />
                    </MDBProgress>

                    <MDBCardText
                      className="mb-1 mt-4"
                      style={{ fontSize: ".77rem" }}
                    >
                      Backend API
                    </MDBCardText>
                    <MDBProgress className="rounded">
                      <MDBProgressBar width={66} valuemin={0} valuemax={100} />
                    </MDBProgress>
                  </MDBCardBody>
                </MDBCard>
              </MDBCol>

              <MDBCol md="6">
                <MDBCard className="mb-md-0 mb-4">
                  <MDBCardBody>
                    <MDBCardText
                      className="mb-4"
                      style={{ fontWeight: "bold" }}
                    >
                      Certifications
                    </MDBCardText>
                    <Card style={{ marginBottom: "4px" }}>
                      <Card.Header>Test Certification</Card.Header>
                      <ListGroup variant="flush">
                        <ListGroup.Item>Validity - 13/July/2027</ListGroup.Item>
                      </ListGroup>
                    </Card>

                    <Card style={{ marginBottom: "4px" }}>
                      <Card.Header>Test Certification</Card.Header>
                      <ListGroup variant="flush">
                        <ListGroup.Item>Validity - 13/July/2027</ListGroup.Item>
                      </ListGroup>
                    </Card>
                  </MDBCardBody>
                </MDBCard>
              </MDBCol>
            </MDBRow>
          </MDBCol>
        </MDBRow>
      </MDBContainer>
    </section>
  );
};

export default Profile;
