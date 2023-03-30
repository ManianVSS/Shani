import React from "react";
import { Col, Container, Row } from "react-bootstrap";
import BootstrapCard from "../../components/BootstrapCard";
import { category2Data } from "../../data/category2";
import { Route, Switch, useParams } from "react-router-dom";
import { useRecoilValue } from "recoil";
import { allPagesData } from "../../state/allPagesData";

const Category2 = () => {
  const { categoryName } = useParams();
  const allPages = useRecoilValue(allPagesData);

  let pageData = allPages.filter((page) => {
    return page.name === categoryName;
  });
  console.log(pageData);
  return (
    <div>
      <h1>{categoryName}</h1>
      <h2>{pageData[0]?.description}</h2>
      <Container>
        <Row className="justify-content-md-center">
          {pageData[0]?.display_items.map((item) => {
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
