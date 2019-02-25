function newlogdiff = bxArith(subid,subsess,logdiff)

% logdiff is a 2-element vector (one for ansview = center and the other for ansview = side)
%
% Joonkoo Park
% 10/25/2011
%

%% Set subject ID and session number, and save data file

workdir = fileparts(which(mfilename));
datadir = [workdir filesep 'data'];
if ~exist(datadir,'dir')
    mkdir(datadir);
end

if nargin < 2
    prompt    = {'Enter participant number :','Enter session number :'};
    dlg_title = 'Participant Information';
    num_lines = 1;
    def       = {'0','0'};
    answer    = inputdlg(prompt,dlg_title,num_lines,def);
    subid     = str2num(answer{1});
    subsess   = str2num(answer{2});
end
if nargin < 3 && subsess > 1
    error('For session number greater than 1, you must input logdiff as the third argument.');
elseif nargin < 3 && subsess <= 1
    logdiff = [1.5 1.5];
end

% Result file names
res_fn_mat = fullfile(datadir,sprintf('%s-debug-%03g-%02g.mat',mfilename,subid,subsess));
res_fn_txt = fullfile(datadir,sprintf('%s-%03g-%02g.txt',mfilename,subid,subsess));

% Check whether result files already exists for this subject/session
if ~(subid == 0 && subsess == 0)
    while exist(res_fn_mat,'file') || exist(res_fn_txt,'file')
        % Construct a questdlg with three options
        choice = questdlg('File exists. Overwrite?', ...
         'File exists', ...
         'Yes, Overwrite', 'No, Quit', 'No, Quit');
        % Handle response
        switch choice
            case 'Yes, Overwrite'
                overwrite = true;
            case 'No, Quit'
                overwrite = false;
        end
        if overwrite
            break;
        else
            fprintf('Terminating...\n');
            return;
        end
    end
end
clear overwrite;

% Construct data struct
data.subid     = subid;
data.subsess   = subsess;
data.datetime  = datestr(now,31);
data.header    = {'Problem','Type','Num1','Num2','Ans1','Ans2','logDiff1','logDiff2','Cresp','Resp','RT','Accuracy'};

%% Set parameters

params.workdir = workdir;
params.datadir = datadir;

% Screen index (use secondary monitor if it exists)
params.screen.idx = max(Screen('Screens'));

% Key parameters
if isequal(computer, 'MACI')
    params.button.keyNext   = 'RightArrow';
    params.button.keyBack   = 'LeftArrow';
else
    params.button.keyNext   = 'right';
    params.button.keyBack   = 'left';
end

% Text parameters
params.text.instr_font  = 'Arial';
params.text.instr_size  = 24;
params.text.instr_color = [255 255 255];
params.text.probe_font  = 'Arial';
params.text.probe_size  = 24;
params.text.probe_color = 255;

% Trial parameters
params.trials.numpractice = 10;
params.trials.numtrials   = 20;
params.trials.numblocks   = 10;

% Size parameters (pixels)
params.size.arraywidth = 310;
params.size.boxwidth   = 320;
params.size.dot        = [4 5 6];
params.size.interdot   = [14 18 21];

% Timing parameters
params.timing.showdots  = 1.0;
params.timing.showprobe = 1.5;
params.timing.maxtrial  = 4.0;
params.timing.feedback  = 0.5;

% Write to File
foutid = fopen(res_fn_txt, 'w');
fprintf(foutid, '# Subject : %05g\r\n', data.subid);
fprintf(foutid, '# Session : %02g\r\n', data.subsess);
fprintf(foutid, '# Date    : %s\r\n', data.datetime);
fprintf(foutid, '%s %s %s %s %s %s %s %s %s %s %s %s\r\n', data.header{:});

%% PsychToolBox device setup

try

    % Get color indices
    dev.white = WhiteIndex(params.screen.idx);
    dev.black = BlackIndex(params.screen.idx);
    dev.gray  = floor((dev.white + dev.black) / 2);
    dev.red   = [255 0 0];
    dev.green = [0 255 0];
    dev.blue  = [0 0 255];

    % Open window
    dev.win = Screen('OpenWindow', params.screen.idx, dev.black);
    
    % Enable alpha blending with proper blend-function
    Screen('BlendFunction', dev.win, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    Screen('Preference', 'TextRenderer', 1);
    Screen('Preference', 'TextAlphaBlending', 1);
    Screen('Preference', 'TextAntiAliasing', [], 1);
    
    % Disable keyboard input to Matlab
    if isequal(computer, 'PCWIN')
        ListenChar(2);
        % HideCursor;
    end

    % Get flip interval and set waitframes
    dev.flipint    = Screen('GetFlipInterval', dev.win);
    dev.waitframes = 1;

    % Get screen dimensions (in pixels)
    [params.screen.width params.screen.height] = Screen('WindowSize', dev.win);
    params.screen.centerx = params.screen.width / 2;
    params.screen.centery = params.screen.height / 2;

    % Get keys
    dev.keyNext   = KbName(params.button.keyNext);
    dev.keyBack   = KbName(params.button.keyBack);
    dev.keyReturn = KbName('return');
    dev.cont      = KbName('c');
    if isequal(computer, 'MACI')
        dev.keyesc = KbName('escape');
        dev.keybackspace = KbName('delete');
    else
        dev.keyesc = KbName('esc');
        dev.keybackspace = KbName('backspace');
    end
    dev.keyNum    = KbName({'1!','2@','3#','4$','5%','6^','7&','8*','9(','0)'});
    dev.keyNumpad = KbName({'1','2','3','4','5','6','7','8','9','0'});
    dev.keyidx    = [dev.keyNum, dev.keyNumpad, dev.keybackspace, dev.keyReturn];
    
    % Graphics position parameters
    params.pos.numleftxy   = [params.screen.width*(1/4), params.screen.height*(1/4)];
    params.pos.numrightxy  = [params.screen.width*(3/4), params.screen.height*(1/4)];
    params.pos.ansleftxy   = [params.screen.width*(1/3), params.screen.height*(3/4)];
    params.pos.ansrightxy  = [params.screen.width*(2/3), params.screen.height*(3/4)];
    params.pos.anscenterxy = [params.screen.width*(1/2), params.screen.height*(3/4)];
    
    params.pos.numleft   = [params.pos.numleftxy(1)-params.size.arraywidth/2, params.pos.numleftxy(2)-params.size.arraywidth/2, ...
        params.pos.numleftxy(1)+params.size.arraywidth/2, params.pos.numleftxy(2)+params.size.arraywidth/2];
    params.pos.numright  = [params.pos.numrightxy(1)-params.size.arraywidth/2, params.pos.numrightxy(2)-params.size.arraywidth/2, ...
        params.pos.numrightxy(1)+params.size.arraywidth/2, params.pos.numrightxy(2)+params.size.arraywidth/2];
    
    params.pos.boxcenter = [params.screen.width*(1/2)-params.size.boxwidth/2, params.screen.height*(1/4)-params.size.boxwidth/2, ...
        params.screen.width*(1/2)+params.size.boxwidth/2, params.screen.height*(1/4)+params.size.boxwidth/2];
    
    params.pos.anscenter = [params.pos.anscenterxy(1)-params.size.boxwidth/2, params.pos.anscenterxy(2)-params.size.boxwidth/2, ...
        params.pos.anscenterxy(1)+params.size.boxwidth/2, params.pos.anscenterxy(2)+params.size.boxwidth/2];
    params.pos.ansleft   = [params.pos.ansleftxy(1)-params.size.arraywidth/2, params.pos.ansleftxy(2)-params.size.arraywidth/2, ...
        params.pos.ansleftxy(1)+params.size.arraywidth/2, params.pos.ansleftxy(2)+params.size.arraywidth/2];
    params.pos.ansright  = [params.pos.ansrightxy(1)-params.size.arraywidth/2, params.pos.ansrightxy(2)-params.size.arraywidth/2, ...
        params.pos.ansrightxy(1)+params.size.arraywidth/2, params.pos.ansrightxy(2)+params.size.arraywidth/2];

%% Practice Trials

if subsess < 2
    
    % Instructions
    params.instr.expmt{1} = ['Welcome to the experiment!\n\n',...
        'You may press the Right Arrow key (next) and the Left Arrow key (back) to navigate through the instruction pages.\n\n',...
        'In this experiment, you will be asked to mentally ADD or SUBTRACT two numerical values represented in dot arrays ',...
        'and to respond with a mouse click.\n\n',...
        'Press Right Arrow to continue.'];
    params.instr.expmt{2} = ['On each trial, sets of dots will move into or out of a gray box. ',...
        'You will be asked to estimate the final number of dots in the gray box.\n\n',...
        'In Addition trials, two separate sets of dots will move into the gray box. ',...
        'Here, you will need to estimate the final number of dots in the gray box (by adding the two sets).\n\n',...
        'In Subtraction trials, one set of dots will move into the gray box and a portion of this set will then leave the box. ',...
        'Here, you will need to estimate the final number of dots remaining in the box (by subtracting the two sets).'];
    params.instr.expmt{3} = ['After the dots move in and out of the box, ',...
        'you will be asked whether the resulting number of dots in the gray box is less or more than an exemplar set, '...
        'or whether it is closer to one exemplar set or another.\n\n',...
        'Move your mouse and click the side that you think is the right answer (please ignore the shape of the mouse cursor). ',...
        'Also, note that the size of the dots may vary, but ONLY focus on the "number" of dots regardless of their size or locations.'];
    params.instr.expmt{4} = ['These instructions sound complicated, but it will be straightforward once you do a couple of practice trials. ',...
        'So let''s do some practice trials now.\n\n',...
        'Press the Enter key to start the practice trials.'];

    % Set default font parameters
    Screen('TextStyle', dev.win, 0);
    Screen('TextFont',  dev.win, params.text.instr_font);
    Screen('TextSize',  dev.win, params.text.instr_size);

    vbl = GetSecs;
    ipage = 1;
    while ipage <= length(params.instr.expmt)

        DrawFormattedText(dev.win, params.instr.expmt{ipage}, 'center', 'center', params.text.instr_color, 60, [], [], 1.5);
        vbl = Screen('Flip', dev.win, vbl + dev.flipint);

        keyCode = [];
        if ipage == 1
            dev.keyNav = [dev.keyNext dev.keyesc];
        elseif ipage > 1 && ipage < length(params.instr.expmt)
            dev.keyNav = [dev.keyNext dev.keyBack dev.keyesc];
        elseif ipage == length(params.instr.expmt)
            dev.keyNav = [dev.keyReturn dev.keyBack dev.keyesc];
        end
        while ~any(ismember(dev.keyNav, find(keyCode)))
            [secs keyCode deltaSecs] = KbWait([],3);
        end

        if keyCode(dev.keyBack)
            ipage = ipage - 1;
        elseif keyCode(dev.keyNext)
            ipage = ipage + 1;
        elseif any(keyCode(dev.keyReturn))
            break;
        elseif keyCode(dev.keyesc)
            Screen('CloseAll');
            ShowCursor;
            ListenChar(0);
            Priority(0);
            return;
        end
    end

    % Set stimulus dimensions
    numrange = (9 : 18)';
    stimset  = [kron(numrange,ones(numel(numrange),1)), repmat(numrange,numel(numrange),1)];
    stimdim  = [ones(size(stimset,1),1), stimset, stimset(:,1) + stimset(:,2); ...
        2*ones(size(stimset,1),1), stimset(:,1) + stimset(:,2), stimset];
    stimdim  = stimdim(randperm(size(stimdim,1)),:);

    Screen('TextFont',  dev.win, params.text.probe_font);
    Screen('TextSize',  dev.win, params.text.probe_size);

    ShowCursor('Arrow');
    vbl = GetSecs;

    for itrial = 1 : params.trials.numpractice

        % Run trials
        stimonset = vbl + 0.5;
        [resp, out, dev] = runTrial(dev, params, stimdim(itrial,:), logdiff, stimonset);

        % Write on file output
        fprintf(foutid, '%g\t%g\t%g\t%g\t%g\t%g\t%.2f\t%.2f\t%s\t%s\t%.3f\t%g\r\n', ...
            0, stimdim(itrial,1:3), out.ans1, out.ans2, logdiff, out.cresp, resp.click, resp.rt, resp.acc);

        if resp.acc == 1
            vbl = displayFeedback(dev, params, 'Correct!');
        else
            vbl = displayFeedback(dev, params, 'Wrong!');
        end

        vbl = displayFixation(dev, params, vbl + params.timing.feedback);
    end
end

%% Real Trials
    
% Instructions
params.instr = [];
if subsess < 2
    params.instr.expmt{1} = ['That was the end of the practice. Let the experimenter know if you have any questions.\n\n',...
        'In the real experiment, you will do these same tasks, but will do more trials.\n\n',...
        'The difficulty of the game will be adjusted by your performance. ',...
        'If you do well, it will become more difficult. If you do not do well, then it will become easier.\n\n',...
        'Please try your best throughout the entire session. ',...
        'Your goal is to improve your performance as much as you can.\n\n',...
        'Press Right Arrow to continue.'];
    params.instr.expmt{2} = ['The trials will be separated into blocks. ',...
        'Each block will contain ' num2str(params.trials.numtrials) ' trials, and you will do a total of ' ...
        num2str(params.trials.numblocks) ' blocks in this session.\n\n',...
        'You have a maximum of ' num2str(params.timing.maxtrial) ' seconds in each trial. ',...
        'Within this time frame, do your best to choose the correct answer. ',...
        'You will also get a feedback as to whether your choice was correct or incorrect.'];
    params.instr.expmt{3} = ['Please ask the experimenter if you have any questions.\n\n',...
        'Otherwise, press the Enter key to start the game.'];
else
    params.instr.expmt{1} = ['Welcome back!\n\n',...
        'You will do the same task that you did in the previous session(s).\n\n',...
        'On each trial, sets of dots will move into or out of a gray box, ',...
        'and you will be asked to estimate the final number of dots in the gray box, ',...
        'by mentally adding or subtracting two numerical values represented in dot arrays.'];
    params.instr.expmt{2} = ['You have a maximum of ' num2str(params.timing.maxtrial) ' seconds in each trial. ',...
        'Within this time frame, do your best to choose the correct answer. ',...
        'Your goal is to improve your performance as much as you can.\n\n',...
        'Please ask the experimenter if you have any questions. ',...
        'Otherwise, press the Enter key to start the game.'];
end

% Set default font parameters
Screen('TextStyle', dev.win, 0);
Screen('TextFont',  dev.win, params.text.instr_font);
Screen('TextSize',  dev.win, params.text.instr_size);

vbl = GetSecs;
ipage = 1;
while ipage <= length(params.instr.expmt)

    DrawFormattedText(dev.win, params.instr.expmt{ipage}, 'center', 'center', params.text.instr_color, 60, [], [], 1.5);
    vbl = Screen('Flip', dev.win, vbl + dev.flipint);

    keyCode = [];
    if ipage == 1
        dev.keyNav = [dev.keyNext dev.keyesc];
    elseif ipage > 1 && ipage < length(params.instr.expmt)
        dev.keyNav = [dev.keyNext dev.keyBack dev.keyesc];
    elseif ipage == length(params.instr.expmt)
        dev.keyNav = [dev.keyReturn dev.keyBack dev.keyesc];
    end
    while ~any(ismember(dev.keyNav, find(keyCode)))
        [secs keyCode deltaSecs] = KbWait([],3);
    end

    if keyCode(dev.keyBack)
        ipage = ipage - 1;
    elseif keyCode(dev.keyNext)
        ipage = ipage + 1;
    elseif any(keyCode(dev.keyReturn))
        break;
    elseif keyCode(dev.keyesc)
        Screen('CloseAll');
        ShowCursor;
        ListenChar(0);
        Priority(0);
        return;
    end
end

Screen('TextFont',  dev.win, params.text.probe_font);
Screen('TextSize',  dev.win, params.text.probe_size);

ShowCursor('Arrow');
vbl = GetSecs;

for iblock = 1 : params.trials.numblocks

    % Set stimulus dimensions
    numrange = (9 : 18)';
    stimset  = [kron(numrange,ones(numel(numrange),1)), repmat(numrange,numel(numrange),1)];
    stimdim  = [ones(size(stimset,1),1), stimset, stimset(:,1) + stimset(:,2); ...
        2*ones(size(stimset,1),1), stimset(:,1) + stimset(:,2), stimset];
    stimdim  = stimdim(randperm(size(stimdim,1)),:);

    % Correct response tally
    coranstype1 = [];
    coranstype2 = [];
    
    fprintf('Block %2g: logdiff = [%g,%g]\n', iblock, logdiff);
    for itrial = 1 : params.trials.numtrials

        % Run trials
        stimonset = vbl + 0.5;
        [resp, out, dev] = runTrial(dev, params, stimdim(itrial,:), logdiff, stimonset);

        % Write on file output
        fprintf(foutid, '%g\t%g\t%g\t%g\t%g\t%g\t%.2f\t%.2f\t%s\t%s\t%.3f\t%g\r\n', ...
            iblock, stimdim(itrial,1:3), out.ans1, out.ans2, logdiff, out.cresp, resp.click, resp.rt, resp.acc);

        if resp.acc == 1
            vbl = displayFeedback(dev, params, 'Correct!');
        else
            vbl = displayFeedback(dev, params, 'Wrong!');
        end

        vbl = displayFixation(dev, params, vbl + params.timing.feedback);

        if out.anstype == 1
            % dots on center
            if resp.acc == 1
                coranstype1 = [coranstype1; 1];
            else
                coranstype1 = [coranstype1; 0];
            end
        else
            % dots on sides
            if resp.acc == 1
                coranstype2 = [coranstype2; 1];
            else
                coranstype2 = [coranstype2; 0];
            end
        end
%         disp(resp);
%         disp(out);
    end
    
%     fprintf('coranstype1, mean = %g\n', mean(coranstype1));
%     fprintf('coranstype2, mean = %g\n', mean(coranstype2));
    
    % Compute performance and adjust logdiff
    if mean(coranstype1) <= .7
        logdiff(1) = min(logdiff(1) + 0.10 + 0.01*ceil(5*rand-3), 2.0);
    elseif mean(coranstype1) >= .85
        logdiff(1) = max(logdiff(1) - 0.15 + 0.01*ceil(5*rand-3), 0.1);
    end
    if mean(coranstype2) <= .7
        logdiff(2) = min(logdiff(2) + 0.10 + 0.01*ceil(5*rand-3), 2.0);
    elseif mean(coranstype2) >= .85
        logdiff(2) = max(logdiff(2) - 0.15 + 0.01*ceil(5*rand-3), 0.1);
    end
    
    newlogdiff = logdiff;
    endofblock(nanmean([mean(coranstype1),mean(coranstype2)]));
end

fprintf('##################################\n');
fprintf('## newlogdiff : [%.2f,%.2f]\n', newlogdiff);
fprintf('##################################\n');
fprintf(foutid, '# newlogdiff : [%.2f,%.2f]\r\n', newlogdiff);
endofexp();

fclose(foutid);

    
catch % ptbexception
    Screen('CloseAll');
    fclose(foutid);
    ShowCursor;
    ListenChar(0);
    Priority(0);
    save(res_fn_mat, 'data', 'params', 'dev');
    assignin('base', 'data', data);         % DEBUG
    assignin('base', 'dev', dev);           % DEBUG
    assignin('base', 'params', params);     % DEBUG
    if exist('ptbexception','var')
        rethrow(ptbexception);
    else
        psychrethrow(psychlasterror);
    end
end % end of try-catch


%% Cleanup

% Close window
Screen('CloseAll');

% Show cursor
ShowCursor;

% Enable keyboard input to Matlab
ListenChar(0);

% Reset priority
Priority(0);

% save data at the workspace
assignin('base', 'data', data);     % DEBUG

%% Nested Functions

    function endofblock(acc)
        
        Screen('TextFont',  dev.win, params.text.instr_font);
        Screen('TextSize',  dev.win, params.text.instr_size);
    
        if acc >= .85
            blockendtext = ['Great job! Your overall accuracy was over 85% in this block. ',...
                'The next block will be slightly harder, ',...
                'so keep up the good work and try to maximize your performance again.\n\n',...
                'Take some time to relax, and press Enter when ready to proceed.'];
        elseif acc <= .7
            blockendtext = ['Your overall accuracy was below 70%. ',...
                'The next block will be slightly easier, ',...
                'so please do your best to improve your performance.\n\n',...
                'Take some time to relax, and press Enter when ready to proceed.'];
        else
            blockendtext = ['Your overall accuracy was around 70~85%. ',...
                'We will keep the difficulty at this level, ',...
                'but remember that your job is to keep improving over time.\n\n',...
                'Take some time to relax, and press Enter when ready to proceed.'];
        end

        DrawFormattedText(dev.win, blockendtext, 'center', 'center', params.text.instr_color, 40, [], [], 1.5);
        Screen('Flip', dev.win);
        
        [keyIsDown secs keyCode deltaSecs] = KbCheck;
        while ~any(ismember([dev.keyReturn], find(keyCode)))
            [secs keyCode deltaSecs] = KbWait([],3);
        end
    end

    function endofexp()
        
        Screen('TextFont',  dev.win, params.text.instr_font);
        Screen('TextSize',  dev.win, params.text.instr_size);
    
        blockendtext = ['This is the end of this session. Please let the experimenter know.'];

        DrawFormattedText(dev.win, blockendtext, 'center', 'center', params.text.instr_color, 40, [], [], 1.5);
        Screen('Flip', dev.win);
        
        [keyIsDown secs keyCode deltaSecs] = KbCheck;
        while ~any(ismember([dev.cont], find(keyCode)))
            [secs keyCode deltaSecs] = KbWait([],3);
        end
    end

end


%% Sub-functions


function [resp, out, dev] = runTrial(dev, params, stim, logdiff, onset)

    % Randomize dot size
    dotsizeidx = randperm(3);
    dotsize    = params.size.dot(dotsizeidx);
    interdot   = params.size.interdot(dotsizeidx);
    
    grid_num1 = getDots(params, stim(2), interdot(1));
    grid_num2 = getDots(params, stim(3), interdot(2));
    
    Screen('FillRect', dev.win, dev.gray, params.pos.boxcenter);
    vbl = Screen('Flip', dev.win, onset);
    
    % Problem
    switch stim(1)
        case 1
            % Addition
            if rand() > .5
                pos1 = 'numleftxy';
                pos2 = 'numrightxy';
            else
                pos1 = 'numrightxy';
                pos2 = 'numleftxy';
            end
            % Show first array
            Screen('DrawDots', dev.win, grid_num1, dotsize(1), dev.white, params.pos.(pos1), 1);
            Screen('FillRect', dev.win, dev.gray, params.pos.boxcenter);
            Screen('DrawingFinished', dev.win);
            vbl = Screen('Flip', dev.win, vbl + 0.2);
            % Move first array
            xpos = linspace(params.pos.(pos1)(1),params.screen.centerx,20);
            for itime = 1 : length(xpos)
                Screen('DrawDots', dev.win, grid_num1, dotsize(1), dev.white, [xpos(itime) params.pos.(pos1)(2)], 1);
                Screen('FillRect', dev.win, dev.gray, params.pos.boxcenter);
                Screen('DrawingFinished', dev.win);
                if itime == 1
                    vbl = Screen('Flip', dev.win, vbl + params.timing.showdots);
                else
                    vbl = Screen('Flip', dev.win, vbl + 0.001);
                end
            end
            % Show second array
            Screen('DrawDots', dev.win, grid_num2, dotsize(2), dev.white, params.pos.(pos2), 1);
            Screen('FillRect', dev.win, dev.gray, params.pos.boxcenter);
            Screen('DrawingFinished', dev.win);
            vbl = Screen('Flip', dev.win, vbl + 0.2);
            % Move second array
            xpos = linspace(params.pos.(pos2)(1),params.screen.centerx,20);
            for itime = 1 : length(xpos)
                Screen('DrawDots', dev.win, grid_num2, dotsize(2), dev.white, [xpos(itime) params.pos.(pos2)(2)], 1);
                Screen('FillRect', dev.win, dev.gray, params.pos.boxcenter);
                Screen('DrawingFinished', dev.win);
                if itime == 1
                    vbl = Screen('Flip', dev.win, vbl + params.timing.showdots);
                else
                    vbl = Screen('Flip', dev.win, vbl + 0.001);
                end
            end
        case 2
            % Subtraction
            if rand() > .5
                pos1 = 'numleftxy';
                pos2 = 'numrightxy';
            else
                pos1 = 'numrightxy';
                pos2 = 'numleftxy';
            end
            % Show first array
            Screen('DrawDots', dev.win, grid_num1, dotsize(1), dev.white, params.pos.(pos1), 1);
            Screen('FillRect', dev.win, dev.gray, params.pos.boxcenter);
            Screen('DrawingFinished', dev.win);
            vbl = Screen('Flip', dev.win, vbl + 0.2);
            % Move first array
            xpos = linspace(params.pos.(pos1)(1),params.screen.centerx,20);
            for itime = 1 : length(xpos)
                Screen('DrawDots', dev.win, grid_num1, dotsize(1), dev.white, [xpos(itime) params.pos.(pos1)(2)], 1);
                Screen('FillRect', dev.win, dev.gray, params.pos.boxcenter);
                Screen('DrawingFinished', dev.win);
                if itime == 1
                    vbl = Screen('Flip', dev.win, vbl + params.timing.showdots);
                else
                    vbl = Screen('Flip', dev.win, vbl + 0.001);
                end
            end
            % Show second array
            Screen('FillRect', dev.win, dev.gray, params.pos.boxcenter);
            vbl = Screen('Flip', dev.win, vbl + 0.2);
            % Move second array
            xpos = linspace(params.screen.centerx,params.pos.(pos2)(1),20);
            for itime = 1 : length(xpos)
                Screen('DrawDots', dev.win, grid_num2, dotsize(2), dev.white, [xpos(itime) params.pos.(pos2)(2)], 1);
                Screen('FillRect', dev.win, dev.gray, params.pos.boxcenter);
                Screen('DrawingFinished', dev.win);
                if itime == 1
                    vbl = Screen('Flip', dev.win, vbl + params.timing.showdots);
                else
                    vbl = Screen('Flip', dev.win, vbl + 0.001);
                end
            end
    end
    
    Screen('FillRect', dev.win, dev.gray, params.pos.boxcenter);
    vbl = Screen('Flip', dev.win, vbl + 0.5);
    
    % Generate Answer Options
    if rand() > .5
        % One array on the center
        ansview = 'center';
        anstype = 1;
        if rand() > .5
            ans1  = round(2^(log2(stim(4)) + logdiff(anstype)));
            cresp = 'left';
        else
            ans1  = round(2^(log2(stim(4)) - logdiff(anstype)));
            cresp = 'right';
        end
        ans2 = NaN;
        if ans1 > 100
            dotsize(3) = 4;
            interdot(3) = 14;
        end
        grid_ans1 = getDots(params, ans1, interdot(3));
    else
        % Two arracys on each side
        ansview = 'side';
        anstype = 2;
        rndidx = rand();
        if rndidx < 1/4
            ans1 = round(2^(log2(stim(4)) + logdiff(anstype)));
            ans2 = stim(4);
            cresp = 'right';
        elseif rndidx < 1/2
            ans1 = round(2^(log2(stim(4)) - logdiff(anstype)));
            ans2 = stim(4);
            cresp = 'right';
        elseif rndidx < 3/4
            ans1 = stim(4);
            ans2 = round(2^(log2(stim(4)) + logdiff(anstype)));
            cresp = 'left';
        else
            ans1 = stim(4);
            ans2 = round(2^(log2(stim(4)) - logdiff(anstype)));
            cresp = 'left';
        end
        if ans1 > 100 || ans2 > 100
            dotsize(3) = 4;
            interdot(3) = 14;
        end
        grid_ans1 = getDots(params, ans1, interdot(3));
        grid_ans2 = getDots(params, ans2, interdot(3));
    end
    
    text1 = '  Less\nthan this';
    text2 = '  More\nthan this';
    textc = 'Which is\ncorrect?';
    switch ansview
        case 'center'
            Screen('DrawDots', dev.win, grid_ans1, dotsize(3), dev.white, params.pos.anscenterxy, 1);
            Screen('FillRect', dev.win, dev.gray, params.pos.boxcenter);
            textBound = [0 0 92 48];
            DrawFormattedText(dev.win, text1, params.pos.ansleftxy(1) - textBound(3)/2, params.pos.ansleftxy(2) - textBound(4)/2, dev.white);
            DrawFormattedText(dev.win, text2, params.pos.ansrightxy(1) - textBound(3)/2, params.pos.ansrightxy(2) - textBound(4)/2, dev.white);
            Screen('DrawingFinished', dev.win);
        case 'side'
            Screen('DrawDots', dev.win, grid_ans1, dotsize(3), dev.white, params.pos.ansleftxy, 1);
            Screen('DrawDots', dev.win, grid_ans2, dotsize(3), dev.white, params.pos.ansrightxy, 1);
            Screen('FillRect', dev.win, dev.gray, params.pos.boxcenter);
            textBound = Screen('TextBounds', dev.win, textc);
            DrawFormattedText(dev.win, textc, 'center', params.pos.anscenterxy(2) - textBound(4)/2, dev.white);
            Screen('DrawingFinished', dev.win);
    end
    probeonset = Screen('Flip', dev.win, vbl);
    
    % Get Mouse Response
%     SetMouse(params.screen.centerx,params.screen.centery);
    resp.click = [];
    [x,y,buttons] = GetMouse(dev.win);
    while true
        [x,y,buttons] = GetMouse(dev.win);
        if buttons(1) && (x > params.pos.ansleft(1) && x < params.pos.ansleft(3)) && (y > params.pos.ansleft(2) && y < params.pos.ansleft(4))
            resp.click = 'left';
            resp.rt    = GetSecs - probeonset;
            break;
        elseif buttons(1) && (x > params.pos.ansright(1) && x < params.pos.ansright(3)) && (y > params.pos.ansright(2) && y < params.pos.ansright(4))
            resp.click = 'right';
            resp.rt    = GetSecs - probeonset;
            break;
        end
        [keyIsDown secs keyCode] = KbCheck;
        if keyCode(dev.keyesc)
            error('Terminated by user');
        end
        
        if secs > probeonset + params.timing.showprobe
            switch ansview
                case 'center'
                    Screen('FillRect', dev.win, dev.gray, params.pos.boxcenter);
                    textBound = [0 0 92 48];
                    DrawFormattedText(dev.win, text1, params.pos.ansleftxy(1) - textBound(3)/2, params.pos.ansleftxy(2) - textBound(4)/2, dev.white);
                    DrawFormattedText(dev.win, text2, params.pos.ansrightxy(1) - textBound(3)/2, params.pos.ansrightxy(2) - textBound(4)/2, dev.white);
                    Screen('DrawingFinished', dev.win);
                case 'side'
                    Screen('FillRect', dev.win, dev.gray, params.pos.boxcenter);
                    textBound = Screen('TextBounds', dev.win, textc);
                    DrawFormattedText(dev.win, textc, 'center', params.pos.anscenterxy(2) - textBound(4)/2, dev.white);
                    Screen('FrameArc', dev.win, dev.white, params.pos.ansleft, 0, 360);
                    Screen('FrameArc', dev.win, dev.white, params.pos.ansright, 0, 360);
                    Screen('DrawingFinished', dev.win);
            end
            vbl = Screen('Flip', dev.win);
        end
        
%         WaitSecs(params.timing.loopwait);
%         WaitSecs(0.1);
%         disp((x > params.pos.ansleft(1) && x < params.pos.ansleft(3)) && (y > params.pos.ansleft(2) && y < params.pos.ansleft(4)));
        if secs > probeonset + params.timing.maxtrial
            resp.click = 'null';
            resp.rt    = NaN;
            break;
        end
    end
    
    if strcmp(cresp, resp.click)
        resp.acc = 1;
    else
        resp.acc = 0;
    end
    out.ans1    = ans1;
    out.ans2    = ans2;
    out.cresp   = cresp;
    out.anstype = anstype;
    
    fprintf('Type=%g\tNum1=%g\tNum2=%g\tlogdiff=%.2f [Ans1=%g,Ans2=%g]\tRT=%.3f\tAcc=%g\n', ...
        stim(1), stim(2), stim(3), logdiff(anstype), ans1, ans2, resp.rt, resp.acc);
    
end



function vbl = displayFixation(dev, params, onset)

    % Display Fixation Dot
    Screen('FillRect', dev.win, dev.white, [params.screen.centerx - 5, params.screen.centery - 5, params.screen.centerx + 5, params.screen.centery + 5]);
    if nargin < 3
        vbl = Screen('Flip', dev.win);
    else
        vbl = Screen('Flip', dev.win, onset);
    end

end


function vbl = displayFeedback(dev, params, feedbacktext, onset)

    % Display Fixation Dot
    DrawFormattedText(dev.win, feedbacktext, 'center', 'center', params.text.probe_color, 60, [], [], 1.5);
    if nargin < 4
        vbl = Screen('Flip', dev.win);
    else
        vbl = Screen('Flip', dev.win, onset);
    end

end


function grid_xy = getDots(params, number, interdot)

    bincount = round(params.size.arraywidth / interdot);
    
    % Control density/extent
    extrange = sqrt(1./(2.^[0 .5]));
    rndext = extrange(ceil(length(extrange)*rand()));

    % Contruct grid
    grid_x  = round(linspace(-params.size.arraywidth/2, params.size.arraywidth/2, bincount));
    grid_y  = round(linspace(-params.size.arraywidth/2, params.size.arraywidth/2, bincount));
    grid_xy = [repmat(grid_x,1,length(grid_y)); kron(grid_y,ones(1,length(grid_x)))];
    
    % Make it circular
    grid_xy = round(grid_xy + .25 * (params.size.arraywidth/bincount) * sin(2*pi*rand(size(grid_xy))));
    dist_xy = sqrt(sum(grid_xy.^2));
    grid_xy = grid_xy(:,dist_xy < params.size.arraywidth/2 * rndext);
    
    % Rotate for natural looks
    omega   = 2*pi*rand;
    grid_xy = round(grid_xy' * [ sin(omega) cos(omega) ; - cos(omega) sin(omega) ])';
    
    % Select a specified number
%     fprintf('Number of grid points = %g\n', size(grid_xy,2));
    if size(grid_xy,2) > number
        rndidx  = randperm(size(grid_xy,2));
        grid_xy = grid_xy(:,rndidx(1:number));
    else
        grid_xy = NaN;
    end
end



