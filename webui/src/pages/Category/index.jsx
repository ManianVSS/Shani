import React from "react";
import { Col, Container, Row } from "react-bootstrap";
import BootstrapCard from "../../components/BootstrapCard";

import { Route, Switch, useParams } from "react-router-dom";
import { useRecoilValue } from "recoil";
import { allPagesData } from "../../state/allPagesData";
import { CardItem001 } from "../../components/CardItem001";
import CardItem002 from "../../components/CardItem002";
import HeroComponent from "../../components/HeroComponent";
import CardItem003 from "../../components/CardItem003";
import { baseURL } from "../../hooks/baseURL";

const Category2 = () => {
  const { categoryName } = useParams();
  const allPages = useRecoilValue(allPagesData);

  let pageData = allPages.filter((page) => {
    return page.name === categoryName;
  });

  // let fdata = allPages.filter((eachVal) => {
  //   let opt = eachVal.details.some(({ gradingDetails }) =>
  //     gradingDetails.some(({ grade }) => grade === "A")
  //   );
  //   return opt;
  // });

  let fdata = allPages.filter((eachVal) => {
    let opt = eachVal?.pages.some(({ name }) => name === categoryName);
    return opt;
  });

  let sfData = fdata[0]?.pages?.filter((page) => {
    return page.name === categoryName;
  });

  let result = fdata.length === 0 ? pageData : sfData;

  return (
    <div>
      {/* <div
        style={{
          background: "white",
          border: "2px solid #404040",
          borderRadius: "15px",
        }}
      >
        <h1 style={{ textAlign: "center" }}>{categoryName}</h1>
      </div> */}
      {/* <h2>{result[0]?.description}</h2> */}

      <HeroComponent
        headline={categoryName}
        description={result[0]?.description.toUpperCase()}
        images={baseURL + result[0]?.image}
      />

      <Container style={{ marginTop: "35px" }}>
        <Row className="justify-content-md-center">
          {result[0]?.display_items.map((item) => {
            return (
              <Col md="auto" key={item.name}>
                {/* <BootstrapCard name={item.name} summary={item.summary} /> */}

                {/* <CardItem001
                  name={item.name}
                  summary={item.summary}
                  image={"http://localhost:8000" + item.image}
                /> */}
                <CardItem003
                  name={item.name}
                  description={item.summary}
                  image={baseURL + item.image}
                  link={item.link}
                />
              </Col>
            );
          })}
        </Row>
      </Container>
    </div>
  );
};

export default Category2;
