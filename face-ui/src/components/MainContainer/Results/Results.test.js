import React from 'react';
import { shallow, render, mount } from 'enzyme';
import Results from './Results';

describe('Results', () => {
  let props;
  let shallowResults;
  let renderedResults;
  let mountedResults;

  const shallowTestComponent = () => {
    if (!shallowResults) {
      shallowResults = shallow(<Results {...props} />);
    }
    return shallowResults;
  };

  const renderTestComponent = () => {
    if (!renderedResults) {
      renderedResults = render(<Results {...props} />);
    }
    return renderedResults;
  };

  const mountTestComponent = () => {
    if (!mountedResults) {
      mountedResults = mount(<Results {...props} />);
    }
    return mountedResults;
  };  

  beforeEach(() => {
    props = {};
    shallowResults = undefined;
    renderedResults = undefined;
    mountedResults = undefined;
  });

  // Shallow / unit tests begin here
 
  // Render / mount / integration tests begin here
  
});
