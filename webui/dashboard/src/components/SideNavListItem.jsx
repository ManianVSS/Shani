import React from "react";
import { styled } from "baseui";
import { useNavigate } from "react-router-dom";
const SideNavListItem = ({ title, children, url, active }) => {
  const history = useNavigate();
  const handleClick = (url) => {
    history(url);
  };
  return (
    <StyledMenuItem
      $active={active}
      title={title}
      onClick={() => handleClick(url)}
    >
      {children}
      {title}
    </StyledMenuItem>
  );
};
export default SideNavListItem;
const StyledMenuItem = styled("div", (props) => ({
  padding: "1.25rem 2rem",
  background: props.$active ? "#9FA2B4" : "none",
  display: "flex",
  alignItems: "center",
  justifyContent: "flex-start",
  fontSize: "1rem",
  color: props.$active ? "#DDE2FF" : "#A4A6B3",
  cursor: "pointer",
  width: "100%",
  borderLeft: props.$active ? "4px solid #DDE2FF" : "none",
  ":hover": {
    background: "#9FA2B4",
    color: "#DDE2FF",
    borderLeft: "4px solid #DDE2FF",
  },
}));
