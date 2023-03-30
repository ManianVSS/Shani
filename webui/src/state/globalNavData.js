import { atom } from "recoil";
import { IconHome } from "@tabler/icons";

export const globalNavData = atom({
  key: "globalNavData",
  default: [{ label: "Home", icon: IconHome, link: "/" }],
});
