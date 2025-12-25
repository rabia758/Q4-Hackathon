import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Course Overview',
      link: {
        type: 'doc',
        id: 'index', // Corresponds to frontend/docs/index.mdx
      },
      items: [
        'chapter-01-introduction-to-physical-ai-robotics/index',
        'chapter-02-mathematics-for-robotics/index',
        'chapter-03-robot-kinematics/index',
        'chapter-04-robot-dynamics/index',
        'chapter-05-sensors-for-humanoid-robotics/index',
        'chapter-06-actuators-and-mechatronics/index',
        'chapter-07-control-systems-for-robotics/index',
        'chapter-08-locomotion-and-balance/index',
        'chapter-09-perception-and-computer-vision/index',
        'chapter-10-robot-manipulation-and-grasping/index',
        'chapter-11-introduction-to-ros2/index',
        'chapter-12-ai-models-for-robotics/index',
      ],
    },
    'glossary',
    'summary',
  ],
};

export default sidebars;
