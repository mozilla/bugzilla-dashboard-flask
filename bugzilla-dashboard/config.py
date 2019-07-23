# parameters to generate URLs for fetching bugcount for components
BZ_QUERIES = {
  "P1Defect": {
      "label": 'P1s defect',
      "parameters": {
          "f1": 'creation_ts', "o1": 'greaterthaneq', "v1": '-1y',
          "priority": 'P1',
          "resolution": '---',
          "bug_type": 'defect'
      },
  },
  "unassignedBetaBugs": {
      "label": 'Unassigned tracked beta bugs',
      "parameters": {
          "f1": 'cf_tracking_firefox_beta', "o1": 'anyexact',    "v1": '+,blocking',
          "f2": 'cf_status_firefox_beta',   "o2": 'equals',      "v2": 'affected',
          "f3": 'assigned_to',           "o3": 'equals',      "v3": 'nobody@mozilla.org',
      },
  },

  "nightlyNewBug": {
      "label": 'Nightly New Regression',
      "hidden": "true",
      "parameters": {
          "keywords": 'regression,',
          "keywords_type": 'allwords',
          "resolution": '---',

          "f1": 'cf_status_firefox_nightly',   "o1": 'equals',       "v1": 'affected',
          "f2": 'OP',                    "j2": 'OR',
          "f3": 'cf_status_firefox_beta',   "o3": 'equals',       "v3": 'unaffected',
          "f4": 'cf_status_firefox_beta',   "o4": 'equals',       "v4": '?',
          "f5": 'cf_status_firefox_beta',   "o5": 'equals',       "v5": '---',
          "f6": 'CP',
          "f7": 'flagtypes.name',        "o7": 'notsubstring', "v7": 'needinfo',
          "f8": 'cf_tracking_firefox_nightly', "o8": 'notequals',    "v8": '-',
          "f9": 'keywords',              "o9": 'notsubstring', "v9": 'stalled',
      },
  },

  "nightlyCarryOver": {
      "label": 'Nightly carry over',
      "hidden": "true",
      "parameters": {
          "keywords": 'regression,',
          "keywords_type": 'allwords',
          "resolution": '---',
          "f1": 'cf_status_firefox_nightly',   "o1": 'equals',       "v1": 'affected',
          "f2": 'OP', "j2": 'OR', "n2": '1',
          "f3": 'cf_status_firefox_beta',   "o3": 'equals',       "v3": 'unaffected',
          "f4": 'cf_status_firefox_beta',   "o4": 'equals',       "v4": '?',
          "f5": 'cf_status_firefox_beta',   "o5": 'equals',       "v5": '---',
          "f6": 'CP',
          "f7": 'flagtypes.name',        "o7": 'notsubstring', "v7": 'needinfo',
          "f8": 'cf_tracking_firefox_nightly', "o8": 'notequals',    "v8": '-',
          "f9": 'keywords',              "o9": 'notsubstring', "v9": 'stalled',
      },
  },

    "newDefects": {
      "label": 'New defects',
      "hidden": "true",
      "parameters": {
          "f1": 'creation_ts', "o1": 'greaterthaneq', "v1": '-1y',
          "priority": '--',
          "resolution": '---',
          "bug_type": 'defect',
      },
  },

  "needinfo": {
      "label": 'Needinfo',
      "hidden": "true",
      "parameters": {
          "priority": '--',
          "resolution": '---',
          "f1": 'flagtypes.name',   "o1": 'substring', "v1": 'needinfo',
          "f2": 'assigned_to',      "o2": 'equals',    "v2": 'nobody@mozilla.org',
      },
  },

  "P1Task": {
      "label": 'P1s task',
      "parameters": {
          "f1": 'creation_ts', "o1": 'greaterthaneq', "v1": '-1y',
          "priority": 'P1',
          "resolution": '---',
          "bug_type": 'task',
      },
  },
  "P1Enhancement": {
      "label": 'P1s enhancement',
      "parameters": {
          "f1": 'creation_ts', "o1": 'greaterthaneq', "v1": '-1y',
          "priority": 'P1',
          "resolution": '---',
          "bug_type": 'enhancement',
      },
  },
  "sec": {
      "label": 'sec-{critical, high}',
      "parameters": {
          "resolution": '---',
          "keywords_type": 'anywords',
          "keywords": 'sec-critical, sec-high',
      },
  },
}
# Bugzilla URLs
settings = {
    "BZ_HOST": 'https://bugzilla.mozilla.org',
    "COMPONENTS_URL": "https://bugzilla.mozilla.org/rest/product?type=accessible&include_fields=name&include_fields=components&exclude_fields=components.flag_types&exclude_fields=components.description"
}
