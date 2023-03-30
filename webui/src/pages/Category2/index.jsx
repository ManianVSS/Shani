import React from "react";
import { Col, Container, Row } from "react-bootstrap";
import BootstrapCard from "../../components/BootstrapCard";
import { category2Data } from "../../data/category2";

const Category2 = () => {
  return (
    <div>
      <Container>
        <Row className="justify-content-md-center">
          {category2Data.map((item) => {
            return (
              <Col md="auto" key={item.name}>
                <BootstrapCard name={item.name} summary={item.summary} />
              </Col>
            );
          })}
        </Row>
      </Container>
    </div>
  );
};

export default Category2;
