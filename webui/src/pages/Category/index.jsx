import React, { useEffect, useState } from "react";
import { Col, Container, Row } from "react-bootstrap";
import BootstrapCard from "../../components/BootstrapCard";

import { Route, Switch, useNavigate, useParams } from "react-router-dom";
import { useRecoilValue } from "recoil";
import { allPagesData } from "../../state/allPagesData";
import { CardItem001 } from "../../components/CardItem001";
import CardItem002 from "../../components/CardItem002";
import HeroComponent from "../../components/HeroComponent";
import CardItem003 from "../../components/CardItem003";
import { baseURL } from "../../hooks/baseURL";

const Category2 = () => {
  const navigate = useNavigate();
  const { siteid, catalogid, categoryid, pageid } = useParams();
  const allPages = useRecoilValue(allPagesData);
  let siteData = [];
  siteData = allPages.filter((site) => {
    return site.id === parseInt(siteid);
  });

  let catalogData = [];
  let categoryData = [];
  let pageData = [];


  if (catalogid) {
    catalogData = (siteData || [])[0]?.catalogs?.filter((catalog) => {
      return catalog.id === parseInt(catalogid);
    });
    if (categoryid) {
      categoryData = (catalogData || [])[0]?.categories?.filter((category) => {
        return category.id === parseInt(categoryid);
      });

      if (pageid) {
        pageData = (categoryData || [])[0]?.pages?.filter((page) => {
          return page.id === parseInt(pageid);
        });
      }
    }
  }

  // let fdata = allPages.filter((eachVal) => {
  //   let opt = eachVal.details.some(({ gradingDetails }) =>
  //     gradingDetails.some(({ grade }) => grade === "A")
  //   );
  //   return opt;
  // });
  let result = [];
  
  if (pageid) {
    result = pageData ?? [];
  } else if (categoryid && !pageid) {
    result = categoryData ?? [];
  } else if (catalogid && !categoryid) {
    result = catalogData ?? [];
  }

  if (catalogData?.length === 0) {
    navigate("notFound");
  }
  
  document.title = (siteData??[])[0]?.name;
  return (
    <div>
      <HeroComponent
        headline={result[0]?.name.toUpperCase()}
        description={result[0]?.description.toUpperCase()}
        images={baseURL + result[0]?.image}
      />
      {/* <iframe src="https://www.youtube.com/embed/uXWycyeTeCs" ></iframe> */}
      <Container style={{ marginTop: "35px" }}>
        <Row className="justify-content-md-center">
          {result[0]?.display_items.map((item) => {
            return (
              <Col md="auto" key={item.name}>
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
