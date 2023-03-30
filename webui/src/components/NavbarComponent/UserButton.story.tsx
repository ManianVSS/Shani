import { storiesOf } from '@storybook/react';
import attributes from './attributes.json';
import { StoryWrapper } from './StoryWrapper';
import { UserButton } from './UserButton';

storiesOf('UserButton', module).add('UserButton', () => (
  <StoryWrapper attributes={attributes} component={UserButton} />
));