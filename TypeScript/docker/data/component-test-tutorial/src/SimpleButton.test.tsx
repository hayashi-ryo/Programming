import { render, screen } from "@testing-library/react";
import { SimpleButton } from "./SimpleButton";
import userEvent from "@testing-library/user-event";

test("Check Button", async () => {
  // コンポーネントテスト
  render(<SimpleButton />); // 描画
  const simpleButton = screen.getByRole("button"); // 初期値の確認
  expect(simpleButton).toHaveTextContent("OFF");
  await userEvent.click(simpleButton); // ONに変化することの確認
  expect(simpleButton).toHaveTextContent("ON");
});

test("Check Button", async () => {
  // スナップショットテスト
  const view = render(<SimpleButton />);
  expect(view.container).toMatchSnapshot();
});
