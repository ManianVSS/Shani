import React, { useState } from "react";
import FeatureCard from "./FeatureCard";
import Slider from "react-slick";

const settings = {
  dots: true,
  // infinite: true,
  speed: 500,
  slidesToShow: 2,
  slidesToScroll: 1,
  arrows: true,
};
const CustomCarousel = (props) => {
  let data = props?.data ?? [];
  return (
    <div
      style={{
        padding: "30px",
        background: "#999999",
      }}
    >
      <Slider {...settings}>
        {data.map((item) => {
          return (
            <>
              <div style={{ margin: "5px" }}>
                <FeatureCard data={item} />
              </div>
            </>
          );
        })}
      </Slider>
    </div>
  );
};

export default CustomCarousel;
