import React from "react";
import {
  HeaderNavigation,
  ALIGN,
  StyledNavigationItem as NavigationItem,
  StyledNavigationList as NavigationList,
} from "baseui/header-navigation";
import { Avatar } from "baseui/avatar";
import { useStyletron } from "baseui";
import Menu from "baseui/icon/menu";
const DashboardHeader = ({ open, setOpen }) => {
  const [css] = useStyletron();
  return (
    <HeaderNavigation
      className={css({
        width: "100%",
        borderBottom: "none !important",
        marginBottom: "1.5rem",
        "@media (max-width: 768px)": {
          paddingLeft: "0",
        },
      })}
    >
      <NavigationList $align={ALIGN.left}>
        <NavigationItem
          className={css({
            fontSize: "1.5rem",
          })}
        >
          <div
            className={css({
              display: "none",
              "@media (max-width: 768px)": {
                display: "block",
              },
            })}
          >
            <Menu size="1.5rem" onClick={() => setOpen(!open)} />
          </div>
          {/* <span
            className={css({
              display: "block",
              "@media (max-width: 768px)": {
                display: "none",
              },
            })}
          >
            Tickets
          </span> */}
        </NavigationItem>
      </NavigationList>
      <NavigationList $align={ALIGN.center} />
      <NavigationList $align={ALIGN.right}>
        {/* <NavigationItem>
          <Avatar
            name="Jane Doe"
            size="2.5rem"
            src="https://avatars.dicebear.com/api/human/yard.svg?width=285&mood=happy"
          />
        </NavigationItem> */}
      </NavigationList>
    </HeaderNavigation>
  );
};
export default DashboardHeader;
