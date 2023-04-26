import React, { useEffect, useState } from "react";
import { Col, Container, Row } from "react-bootstrap";
import BootstrapCard from "../../components/BootstrapCard";

import { Route, Switch, useNavigate, useParams } from "react-router-dom";
import { useRecoilState, useRecoilValue } from "recoil";
import { allPagesData } from "../../state/allPagesData";
import { CardItem001 } from "../../components/CardItem001";
import HeroComponent from "../../components/HeroComponent";
import CardItem003 from "../../components/CardItem003";
import { baseURL } from "../../hooks/baseURL";
import IframeComponent from "../../components/IframeComponent";
import { useWindowSize } from "../../hooks/windowSize";
import { sideBar } from "../../state/mode";
import TimerComponent from "../../components/TimerComponent";
import { timerState } from "../../state/timerData";
import ResponsiveCarousel from "../../components/Carousel";

const Category2 = () => {
  const navigate = useNavigate();
  const pageSize = useWindowSize();
  const sideBarState = useRecoilValue(sideBar);
  const [timerData, setTimerData] = useRecoilState(timerState);
  const { siteid, catalogid, categoryid, pageid } = useParams();
  const allPages = useRecoilValue(allPagesData);
  let siteData = [];
  siteData = allPages.filter((site) => {
    return site.id === parseInt(siteid);
  });

  let catalogData = [];
  let categoryData = [];
  let pageData = [];
  let eventsData = [];

  if (catalogid) {
    catalogData = (siteData || [])[0]?.catalogs?.filter((catalog) => {
      return catalog.id === parseInt(catalogid);
    });
    eventsData = (catalogData || [])[0]?.events;
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

  document.title = (siteData ?? [])[0]?.name;
  setTimerData((eventsData ?? [])[0]?.time);

  return (
    <>
      {result[0]?.iframe_link?.length === 0 ||
      result[0]?.iframe_link?.length === undefined ? (
        <>
          {(eventsData ?? []).length === 0 ? (
            <></>
          ) : (
            // <TimerComponent name={(eventsData ?? [])[0]?.name} />
            <ResponsiveCarousel
              autoPlay={true}
              infiniteLoop={true}
              componentListData={eventsData ?? []}
              showArrows={false}
              showStatus={false}
              showIndicators={false}
              showThumbs={false}
            />
          )}

          <HeroComponent
            headline={result[0]?.name.toUpperCase()}
            description={result[0]?.description.toUpperCase()}
            images={baseURL + result[0]?.image}
          />
          <Container style={{ marginTop: "35px" }}>
            <Row className="justify-content-md-center">
              {result[0]?.display_items.map((item) => {
                return (
                  <Col md="auto" key={item.name}>
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
        </>
      ) : (
        <IframeComponent
          link={result[0]?.iframe_link}
          width={sideBar === "open" ? pageSize.width * 0.8 : pageSize.width}
          height={pageSize.height * 0.95}
        />
      )}
    </>
  );
};

export default Category2;
